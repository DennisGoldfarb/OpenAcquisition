import xml.sax
import pkg_resources
import pyopenms as po
import base64
import struct
from openacquisition.mathematics.splines import CubicSpline

def estimateFromPeptideWeight(mono_mass, max_isotope): 
    # Fast approximation using spline models
    if _isotopeSplineDB.inBounds(mono_mass, max_isotope): 
        result = po.IsotopeDistribution()
        result.clear()
          
        for isotope in range(max_isotope+1):
            probability = _isotopeSplineDB.models[isotope].eval(mono_mass)
            iso_mass = mono_mass + (isotope * po.Constants.C13C12_MASSDIFF_U)
            result.insert(iso_mass, probability)
    # Slower approximation using averagine approach from OpenMS      
    else:
        result = po.CoarseIsotopePatternGenerator(max_isotope, False).estimateFromPeptideWeight(mono_mass)
    
    result.renormalize()
    
    return result
    
def estimateForFragmentFromWeights(mono_peptide_mass, mono_fragment_mass, min_isotope, max_isotope):
    fragment_id = estimateFromPeptideWeight(mono_fragment_mass, max_isotope)
    comp_fragment_id = estimateFromPeptideWeight(mono_peptide_mass - mono_fragment_mass, max_isotope)
    return _calcFragmentIsotopeDistribution(fragment_id, comp_fragment_id, min_isotope, max_isotope)
        
def _calcFragmentIsotopeDistribution(fragment_id, comp_fragment_id, min_isotope, max_isotope):
    
    result = po.IsotopeDistribution()
    result.resize(max_isotope + 1)
    container = []
    for i in range(min_isotope, max_isotope+1):
        container.append(po.Peak1D())
    
    for i in range(fragment_id.size()):
        for isotope in range(min_isotope, max_isotope+1):
            if isotope >= i and (isotope - 1) < comp_fragment_id.size():
                container[i].setIntensity(container[i].getIntensity() + comp_fragment_id.getContainer()[isotope-i].getIntensity())

        container[i].setIntensity(container[i].getIntensity() * fragment_id.getContainer()[i].getIntensity())
        container[i].setMZ(fragment_id.getContainer()[0].getMZ() + (i * po.Constants.C13C12_MASSDIFF_U))
    
    result.set(container)
    result.renormalize()

    return result
        
        
        




class IsotopeSplineDB:
    def __init__(self):
        self.models = dict()
        
        parser = xml.sax.make_parser()
        handler = IsotopeSplineXMLHandler(self)
        parser.setContentHandler(handler)
        data_path = pkg_resources.resource_filename('openacquisition.chemistry', "IsotopeSplines_100kDa_21isotopes.xml")
        with open(data_path) as xml_data:
            parser.parse(data_path)
            
    def inBounds(self, mono_mass, max_isotope):
        # check if max isotope is in bounds
        if max_isotope >= len(self.models):
            return False
        
        # check if masses are in bounds
        for isotope in range(max_isotope+1):
            if not self.models[isotope].inBounds(mono_mass):
                return False
        
        # all checks passed
        return True








class IsotopeSplineXMLHandler(xml.sax.ContentHandler):
    def __init__(self, splineDB):
        self.current_tag = ""
        self.splineDB = splineDB
        
    def startElement(self, tag, attributes):
        self.current_tag = tag
        self.contentBuffer = ""
        if self.current_tag == "model":
            self.isotope = int(attributes["isotope"])
        if self.current_tag in ["knots", "coefficients"]:
            self.precision = int(attributes["precision"])
            self.endian = attributes["endian"]
            self.length = int(attributes["length"])
        
    def endElement(self, tag):
        if tag == "knots":
            self.knots = self.decodeDoubleList(self.contentBuffer, self.precision , self.endian, self.length)
        elif tag == "coefficients":
            coefficients = self.decodeDoubleList(self.contentBuffer, self.precision , self.endian, self.length)
            self.splitCoefficients(coefficients)
        elif tag == "model":
            spline = CubicSpline(self.a, self.b, self.c, self.d, self.knots)
            self.splineDB.models[self.isotope] = spline
        
    
    def characters(self, content):
        self.contentBuffer += content
        
    def splitCoefficients(self, coefficients):
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        
        for i in range(0, len(coefficients), 4):
            self.a.append(coefficients[i])
            self.b.append(coefficients[i+1])
            self.c.append(coefficients[i+2])
            self.d.append(coefficients[i+3])
        
    def decodeDoubleList(self, encoded, precision, endian, length):
        decoded = base64.b64decode(encoded)
        
        # ensure valid endian
        assert endian == 'little' or endian == "big"
        if endian == 'little':
            endianChar = "<"
        else:
            endianChar = ">"
            
        # ensure precision is 32 or 64 bit
        assert precision == 32 or precision == 64
        # ensure that there's enough data for 32-bit floats or 64-bit doubles
        if precision == 32:
            assert len(decoded) // 4 == length
            # unpack the data as floats
            result = struct.unpack(endianChar + '{0}f'.format(length), decoded) # one big structure of `count` floats # results returned as a tuple
        elif precision == 64:
            assert len(decoded) // 8 == length
            # unpack the data as floats
            result = struct.unpack(endianChar + '{0}d'.format(length), decoded) # one big structure of `count` doubles # results returned as a tuple
            
        return result
        
    
_isotopeSplineDB = IsotopeSplineDB()    
import pytest
from openacquisition.chemistry.isotopes import *

def test_IsotopeSplineDB_init():
    splineDB = IsotopeSplineDB()
    assert len(splineDB.models) == 21

def test_IsotopeSplineDB_inBounds():
    splineDB = IsotopeSplineDB()
    
    assert splineDB.inBounds(1000, 0) == True
    assert splineDB.inBounds(50, 0) == False
    assert splineDB.inBounds(100000, 0) == True
    assert splineDB.inBounds(100100, 0) == False

def test_estimateFromPeptideWeight():
    id = estimateFromPeptideWeight(1000, 5)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.5643, 1e-4)
    assert id.getContainer()[1].getIntensity() == pytest.approx(0.29824, 1e-4)
    
    id = estimateFromPeptideWeight(2000, 5)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.31678, 1e-4)
    assert id.getContainer()[1].getIntensity() == pytest.approx(0.33796, 1e-4)
    assert id.getContainer()[2].getIntensity() == pytest.approx(0.20790, 1e-4)
    assert id.getContainer()[3].getIntensity() == pytest.approx(0.09331, 1e-4)
    
    id = estimateFromPeptideWeight(50, 5)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.9727, 1e-4)
    
def test_estimateForFragmentFromWeights():
    id = estimateForFragmentFromWeights(200, 100, 0, 0)
    assert id.getContainer()[0].getIntensity() == pytest.approx(1.0, 1e-4)
    
    id = estimateForFragmentFromWeights(200, 100, 0, 1)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.95994, 1e-4)
    
    id = estimateForFragmentFromWeights(2000, 100, 0, 1)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.97883, 1e-4)
    
    id = estimateForFragmentFromWeights(2000, 1000, 0, 1)
    assert id.getContainer()[0].getIntensity() == pytest.approx(0.743077, 1e-4)
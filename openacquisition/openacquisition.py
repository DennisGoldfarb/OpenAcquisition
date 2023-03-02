from yapsy.IPlugin import IPlugin
from abc import ABC, abstractmethod
from typing import Optional, List
from logging import Logger


class APIConverterPlugin(IPlugin):
    @abstractmethod
    def connectToInstrument(self, parameters):
        pass

    @abstractmethod
    def disconnectFromInstrument(self, parameters):
        pass

    @abstractmethod
    def getInstrumentStatus(self, parameters):
        pass

    @abstractmethod
    def submitScanRequest(self, parameters):
        pass
    
    @abstractmethod
    def onScanArrived(self, scan):
        pass
  
    
class AcquisitionMethodPlugin(IPlugin):
    @abstractmethod
    def processScan(self, scan):
        pass

    @abstractmethod
    def onComplete(self):
        pass

    @abstractmethod
    def onScanRequested(self):
        pass


    


class AcquisitionMediator():
    def __init__(self):
        pass


class ScanRequestQueueManager():
    def __init__(self):
        pass


class ScanRequestQueue():
    def __init__(self):
        pass
    
    
class Instrument():
    # initialize from APIConverter and Instrument connection objects
    # initialize from InstrumentConfiguration
    def __init__(self):
        pass
    

class InstrumentConfiguration():
    def __init__(self):
        pass
    
    

    
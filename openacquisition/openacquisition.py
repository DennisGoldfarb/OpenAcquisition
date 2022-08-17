from abc import ABC, abstractmethod





class APIConverter(ABC):
    
    @abstractmethod
    def connect_to_instrument(parameters):
        pass

    @abstractmethod
    def disconnect_from_instrument(parameters):
        pass

    @abstractmethod
    def get_instrument_status(parameters):
        pass

    @abstractmethod
    def submit_scan_request(parameters):
        pass
    
    def on_scan_arrived(scan):
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
    
    

    
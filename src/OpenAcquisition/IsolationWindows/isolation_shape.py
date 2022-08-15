import math

class IsolationShape:
    
    def __init__(self, a, b, c, d):
        """_summary_

        Args:
            a (float): _description_
            b (float): _description_
            c (float): _description_
            d (float): _description_
        """
        self.a = a
        self.b = b
        self.b2 = 2*b
        self.c = c
        self.d = d
        self.offset_range = self.get_offset_range()
    
    def get_isolation_efficiency(self, offset):
        """_summary_

        Args:
            offset (float): _description_

        Returns:
            float: _description_
        """
        return self.d / (1 + math.pow(abs((offset - self.c) / self.a), self.b2))
    
    def get_isolation_efficienct_unshifted(self, offset):
        """_summary_

        Args:
            offset (float): _description_

        Returns:
            float: _description_
        """
        return self.d / (1 + math.pow(abs((offset) / self.a), self.b2))
    
    def get_offset_range(self, efficiency_threshold = 0.01):
        """_summary_

        Args:
            efficiency_threshold (float, optional): _description_. Defaults to 0.01.

        Returns:
            float: _description_
        """
        return self.a * math.pow((self.d / efficiency_threshold - 1), 1 / self.b2)

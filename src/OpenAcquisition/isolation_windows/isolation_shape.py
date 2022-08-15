import math
from lazy import lazy

class IsolationShape:
    
    def __init__(self, a, b, c, d):
        """Generalized bell-shaped function representing the isolation efficiency shape of quadrupole or linear ion trap. 

        Args:
            a (float): half-width at half-maximum
            b (float): proportional to the slope at the edges of the function
            c (float): offset from center
            d (float): full maximum
        """
        self.a = a
        self.b = b
        self.b2 = 2*b
        self.c = c
        self.d = d
    
    def get_isolation_efficiency(self, offset):
        """Computes the isolation efficiency at a given offset from the center of the isolation window.

        Args:
            offset (float): offset from the isolation window's center

        Returns:
            float: isolation efficiency
        """
        return self.d / (1 + math.pow(abs((offset - self.c) / self.a), self.b2))
    
    def get_isolation_efficiency_unshifted(self, offset):
        """Computes the isolation efficiency at a given offset from the center of the isolation efficiency model.
        This ignores the c parameter of the generalized bell-shaped function.

        Args:
            offset (float): offset from the isolation window's center of isolation efficiency

        Returns:
            float: isolation efficiency
        """
        return self.d / (1 + math.pow(abs((offset) / self.a), self.b2))
    
   
    def get_offset_range(self, efficiency_threshold = 0.01):
        """Returns the positive unshifted offset (ignores the c parameter) with the given isolation efficiency threshold.
        Since the generalized bell-shaped function is convex and symmetric, the range from the negative and postive
        values will contain all offsets with efficiency >= efficiency_threshold.

        Args:
            efficiency_threshold (float, optional): minimum isolation efficiency. Defaults to 0.01.

        Returns:
            float: positive unshifted offset with the given isolation efficiency
        """
        return self.a * math.pow((self.d / efficiency_threshold - 1), 1 / self.b2)
    
    @lazy
    def offset_range(self):
        """Returns the positive unshifted offset (ignores the c parameter) with 0.01 isolation efficiency threshold.
        Since the generalized bell-shaped function is convex and symmetric, the range from the negative and postive
        values will contain all offsets with efficiency >= efficiency_threshold.

        Returns:
            float: positive unshifted offset with the given isolation efficiency
        """
        return self.get_offset_range()
    


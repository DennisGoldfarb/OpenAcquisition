import math
from lazy import lazy

class IsolationShape:
    
    def __init__(self, a, b, c, d):
        """Isolation efficiency model constructor
        
        Generalized bell-shaped function representing the isolation efficiency shape of a quadrupole or linear ion trap.

        Parameters
        ----------
        a : float
            half-width at half-maximum
        b : float
            proportional to the slope at the edges of the function
        c : float
            offset from center
        d : float
            full maximum
            
        Notes
        -----
        Let :math:`y = \frac{d}{1+\frac{\left|x-c\right|}{a}^{2b}}`
        where :math:`y` represents the isolation efficiency
        and :math:`x` represents the offset from the center of the window.
        """
       
        self.a = a
        self.b = b
        self.b2 = 2*b
        self.c = c
        self.d = d
    
    def get_isolation_efficiency(self, offset):
        """Computes the isolation efficiency at a given offset from the center of the isolation window.

        Parameters
        ----------
        offset : float
            offset from the isolation window's center

        Returns
        -------
        float
            isolation efficiency
        """
        
        return self.d / (1 + math.pow(abs((offset - self.c) / self.a), self.b2))
    
    def get_isolation_efficiency_unshifted(self, offset):
        """Computes the isolation efficiency at a given offset from the center of the isolation efficiency model.

        Parameters
        ----------
        offset : float
            offset from the isolation window's center of isolation efficiency

        Returns
        -------
        float
            isolation efficiency
            
        Notes
        -----
        This ignores the c parameter of the generalized bell-shaped function.
        """
        return self.d / (1 + math.pow(abs((offset) / self.a), self.b2))
    
   
    def get_offset_range(self, efficiency_threshold = 0.01):
        """Returns the positive unshifted offset (ignores the c parameter) with the given isolation efficiency threshold
        
        Parameters
        ----------
        efficiency_threshold : float, optional
            minimum isolation efficiency, by default 0.01

        Returns
        -------
        float
            positive unshifted offset with the given isolation efficiency
            
        Notes
        -----
        Since the generalized bell-shaped function is convex and symmetric, the range from the negative and postive
        values will contain all offsets with efficiency >= efficiency_threshold.
        """
        return self.a * math.pow((self.d / efficiency_threshold - 1), 1 / self.b2)
    
    
    @lazy
    def offset_range(self):
        """Returns the positive unshifted offset (ignores the c parameter) at 0.01 isolation efficiency
        
        Returns
        -------
        float
            positive unshifted offset at 0.01 isolation efficiency
            
        Notes
        -----
        Lazy evaluation. Will only be computed at first request and then the result will be cached 
        """
        return self.get_offset_range()
    
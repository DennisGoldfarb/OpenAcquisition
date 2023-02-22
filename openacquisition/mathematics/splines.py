from bisect import bisect_left

class CubicSpline:
    def __init__(self, a, b, c, d, knots):     
        # Validate input length
        it = iter([a,b,c,d,knots])
        the_len = len(next(it))
        if not all(len(l) == the_len for l in it):
            raise ValueError('CubicSpline init: Not all input lists have same length.')
        
        self.a = a # constant spline coefficients
        self.b = b # linear spline coefficients
        self.c = c # quadratic spline coefficients
        self.d = d # cubic spline coefficients
        self.knots = knots # knots
     
    def eval(self, x):
        index = bisect_left(self.knots, x) - 1
        
        if index < 0:
            index = 0
        
        xx = x - self.knots[index]

        return ((self.d[index] * xx + self.c[index]) * xx + self.b[index]) * xx + self.a[index];
    
    def inBounds(self, x):
        return x >= self.knots[0] and x <= self.knots[-1]


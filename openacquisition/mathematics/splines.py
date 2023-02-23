from bisect import bisect_right

class CubicSpline:
    def __init__(self, a, b, c, d, knots):     
        # Validate input length
        it = iter([a,b,c,d])
        the_len = len(next(it))
        if not all(len(l) == the_len for l in it):
            raise ValueError('CubicSpline init: Not all input coefficient lists have the same length.')
        if not len(knots) == len(a) + 1:
            raise ValueError('CubicSpline init: knots length should be 1 more than the coefficient lengths.')
        
        self.a = a # constant spline coefficients
        self.b = b # linear spline coefficients
        self.c = c # quadratic spline coefficients
        self.d = d # cubic spline coefficients
        self.knots = knots # knots
     
    # For speed purposes we're not checking if x is in bounds. Assume the programmer has checked this beforehand.
    def eval(self, x):
        index = bisect_right(self.knots, x) - 1
        
        xx = x - self.knots[index]

        return ((self.d[index] * xx + self.c[index]) * xx + self.b[index]) * xx + self.a[index];
    
    def inBounds(self, x):
        return x >= self.knots[0] and x <= self.knots[-1]


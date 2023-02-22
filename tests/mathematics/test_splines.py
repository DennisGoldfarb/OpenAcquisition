import pytest
from openacquisition.mathematics.splines import CubicSpline

def test_init():
    spline = CubicSpline([1,1], [2,2], [3,3], [4,4], [50, 100])
    assert spline.a == [1,1]
    assert spline.b == [2,2]
    assert spline.c == [3,3]
    assert spline.d == [4,4]
    assert spline.knots == [50,100]
    
    # Inputs of varying sizes should raise an error
    with pytest.raises(ValueError) as exc_info:
        spline = CubicSpline([1,1,1], [2,2], [3,3], [4,4], [50, 100])
    
def text_inBounds():
    spline = CubicSpline([1,1], [2,2], [3,3], [4,4], [50, 100])
    assert spline.inBounds(50) == True
    assert spline.inBounds(49) == False
    assert spline.inBounds(100) == True
    assert spline.inBounds(101) == False
    assert spline.inBounds(75) == True
    
def test_eval():
    spline = CubicSpline([1,1], [2,2], [3,3], [4,4], [50, 100])
    assert spline.eval(50) == 1
    assert spline.eval(51) == 10
    assert spline.eval(49) == -2
    
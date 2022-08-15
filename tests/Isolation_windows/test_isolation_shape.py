import pytest
from openacquisition.isolation_windows.isolation_shape import IsolationShape

def test_init():
    shape = IsolationShape(1,10,0,1)
    assert shape.a == 1
    assert shape.b == 10
    assert shape.b2 == 20
    assert shape.c == 0
    assert shape.d == 1
    assert shape.offset_range == pytest.approx(1.258293)
  
  
def test_get_isolation_efficiency():
    shape = IsolationShape(1,10,0,1)
    assert shape.get_isolation_efficiency(0) == pytest.approx(1.0)
    assert shape.get_isolation_efficiency(1) == pytest.approx(0.5)
    
    shape = IsolationShape(1,10,1,1)
    assert shape.get_isolation_efficiency(1) == pytest.approx(1.0)
    assert shape.get_isolation_efficiency(2) == pytest.approx(0.5)
    
    shape = IsolationShape(1,10,-1,1)
    assert shape.get_isolation_efficiency(1) == pytest.approx(9.536734e-7)
    assert shape.get_isolation_efficiency(2) == pytest.approx(2.867972e-10)
    
    shape = IsolationShape(1,10,0,0.5)
    assert shape.get_isolation_efficiency(1) == pytest.approx(0.25)

    
def test_get_isolation_efficiency_unshifted():
    shape = IsolationShape(1,10,0,1)
    assert shape.get_isolation_efficiency_unshifted(0) == pytest.approx(1.0)
    assert shape.get_isolation_efficiency_unshifted(1) == pytest.approx(0.5)
    
    shape = IsolationShape(1,10,1,1)
    assert shape.get_isolation_efficiency_unshifted(1) == pytest.approx(0.5)
    assert shape.get_isolation_efficiency_unshifted(2) == pytest.approx(9.536734e-7)
    
    shape = IsolationShape(1,10,-1,1)
    assert shape.get_isolation_efficiency_unshifted(1) == pytest.approx(0.5)
    assert shape.get_isolation_efficiency_unshifted(2) == pytest.approx(9.536734e-7)
    
    shape = IsolationShape(1,10,0,0.5)
    assert shape.get_isolation_efficiency_unshifted(1) == pytest.approx(0.25)

    
def test_get_offset_range():
    shape = IsolationShape(1,10,0,1)
    assert shape.get_offset_range() == pytest.approx(1.258293)
    assert shape.get_offset_range(0.01) == pytest.approx(1.258293)
    assert shape.get_offset_range(0.001) == pytest.approx(1.4124668)
    
    shape = IsolationShape(1,10,1,1)
    assert shape.get_offset_range() == pytest.approx(1.258293)
    assert shape.get_offset_range(0.01) == pytest.approx(1.258293)
    assert shape.get_offset_range(0.001) == pytest.approx(1.4124668)
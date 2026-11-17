from fuel import gauge, convert
import pytest

def test_str_input():
    # Verify that non-integer strings raise ValueError
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_0_input():
    # Verify that dividing by zero raises ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_improper_fraction():
    # Verify that x > y raises ValueError
    with pytest.raises(ValueError):
        convert('5/4')

def test_negative_fraction():
    # Verify that negative fractions raise ValueError
    # This is the fix for the check50 error!
    with pytest.raises(ValueError):
        convert('-1/2')

def test_convert():
    # Verify correct integer return values
    assert convert('1/2') == 50
    assert convert('1/4') == 25

def test_fulltank():
    # Verify 'F' labeling for 99% and 100%
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_emptytank():
    # Verify 'E' labeling for 1% and 0%
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'

def test_gauge():
    # Verify standard percentage string output
    assert gauge(50) == '50%'

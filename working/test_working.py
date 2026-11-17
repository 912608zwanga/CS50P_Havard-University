import pytest
from working import convert

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 AM to 8:50 AM") == "00:30 to 08:50"

def test_2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_3():
    # Impossible minutes
    with pytest.raises(ValueError):
        convert("8:70 AM to 12:70 PM")
    # Missing spaces
    with pytest.raises(ValueError):
        convert("9AM to 8PM")
    # Already in 24-hour format (should be rejected)
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    # Using a hyphen instead of "to"
    with pytest.raises(ValueError):
        convert("9 AM - 8 PM")
    # Another 24-hour format check
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

if __name__ == "__main__":
    main()

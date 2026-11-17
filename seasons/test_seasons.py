from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    # Test valid date format returns tuple of strings
    assert check_birthday('1998-07-03') == ("1998", "07", "03")

    # Test missing leading zeros returns None
    assert check_birthday('1998-7-3') == None

    # Test invalid format returns None
    assert check_birthday("July 3, 1998") == None

if __name__ == "__main__":
    main()

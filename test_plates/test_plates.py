from plates import is_valid

def test_2letters():
    assert is_valid("CS50") == True

def test_2letters2():
    assert is_valid("C5") == False

def test_max_letters():
    assert is_valid("HELLO") == True

def test_max_letters2():
    assert is_valid("HELLOWORLD") == False

def test_mid_num():
    assert is_valid("AAA222") == True

def test_mid_num2():
    assert is_valid("AAA22A") == False

def test_mid_num3():
    assert is_valid("AAA022") == False

def test_psp():
    assert is_valid("TRUE ?") == False

def test0():
    assert is_valid("") == False

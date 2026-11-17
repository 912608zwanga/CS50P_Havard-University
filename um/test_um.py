from um import count

def main():
    test_1()
    test_2()
    test_3()

def test_1():
    # Test standalone um and case sensitivity
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_2():
    # Test um with punctuation
    assert count("um?") == 1
    assert count("Um... thanks, um.") == 2
    assert count("Hello, um, world") == 1

def test_3():
    # Test um inside other words (should not be counted)
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrument") == 0

if __name__ == "__main__":
    main()

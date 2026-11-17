from bank import value

def test_hello():
    assert value('hello sir') == 0


def test_Hello():
    assert value('Hello sir') == 0


def test_h():
    assert value('how are you sir?') == 20


def test_H():
    assert value('How are you sir?') == 20


def test_value():
    assert value('hello sir') == 0

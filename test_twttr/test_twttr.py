from twttr import shorten

def test_lowercase():
    assert shorten('thanks') == 'thnks'

def test_uppercase():
    assert shorten('GOOD') == 'GD'

def test_num():
    assert shorten('thanks123') == 'thnks123'

def test_punctuation():
    assert shorten('thanks.') == 'thnks.'



#from twttr import shorten

# Test for handling an empty string input
#def test_shorten_empty():
 #   assert shorten("") == "", "Should return an empty string for empty input"

# Test for handling strings with no vowels at all
#def test_shorten_no_vowels():
 #   assert shorten("bcdfg") == "bcdfg", "Should return the same string if no vowels"

# Test for handling strings that consist only of vowels
#def test_shorten_only_vowels():
 #   assert shorten("aeiou") == "", "Should return empty if input is only vowels"

# Test for a standard lowercase word with vowels
#def test_shorten_normal_case():
  #  assert shorten("hello") == "hll", "Should remove lower case vowels"

# Test for handling both uppercase and lowercase vowels in the same string
#def test_shorten_mixed_case():
 #   assert shorten("Hello WORLD") == "Hll WRLD", "Should remove both upper and lower case vowels"

# Test to ensure special characters are preserved while vowels are removed
#def test_shorten_special_chars():
  #  assert shorten("h!e@l#l$%") == "h!l#l$", "Should remove vowels but keep special characters"

# Test to ensure numbers are preserved while vowels are removed
#def test_shorten_numbers():
 #   assert shorten("hello2") == "hll2", "Should remove vowels and keep numbers"

# Test to ensure spaces are preserved correctly
#def test_shorten_with_spaces():
 #   assert shorten("hello world") == "hll wrld", "Should remove vowels and keep spaces"

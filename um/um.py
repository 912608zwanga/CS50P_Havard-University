import re

def main():
    print(count(input("Text: ")))

def count(s):
    # \b is the word boundary anchor.
    # It ensures we catch "um" but skip "yummy" or "hum".
    word_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(word_count)

if __name__ == "__main__":
    main()

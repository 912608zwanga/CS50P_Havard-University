import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Check if the input is an iframe
    if re.search(r"<iframe.*?></iframe>", s):

        # We only need to capture the ID at the very end
        url_pattern = re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)", s)

        if url_pattern:
            # .group(1) specifically targets the first set of (...)
            return "https://youtu.be/" + url_pattern.group(1)

    return None

if __name__ == "__main__":
    main()

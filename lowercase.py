from clipboarder import Clipboarder

def lowercase(string):
    return string.lower()

if __name__ == "__main__":
    c = Clipboarder(lowercase)
    c.run()

import re


class ReplaceWhiteSpace:
    def __init__(self, str1):
        self.str1 = str1

    def replace_whitespace(self):
        return re.sub(r"\s+", '%20', self.str1)


if __name__ == "__main__":
    str1 = str(input("Enter string: "))
    a = ReplaceWhiteSpace(str1)
    print(a.replace_whitespace())

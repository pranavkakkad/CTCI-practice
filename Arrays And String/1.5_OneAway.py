def edit_string(str1, str2):
    change = False
    for i, j in zip(str1, str2):
        if i != j:
            if change:
                return False
            change = True
    return True


def add_char(str1, str2):

    change = False
    i, j = 0, 0
    while i < len(str1) or j < len(str2):
        if str1[i] != str2[j]:
            if change:
                return False
            change = True
            i += 1
        else:
            i += 1
            j += 1
    return True


class OneAway:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def check_function(self):
        if len(self.str1) == len(self.str2):
            return edit_string(self.str1, self.str2)
        if len(self.str1) + 1 == len(self.str2):
            return add_char(self.str1, self.str2)
        if len(self.str1) - 1 == len(self.str2):
            return add_char(self.str1, self.str2)

        return False


if __name__ == "__main__":
    str1 = str(input("Enter string 1: "))
    str2 = str(input("Enter string 2: "))
    a = OneAway(str1, str2)
    print(a.check_function())

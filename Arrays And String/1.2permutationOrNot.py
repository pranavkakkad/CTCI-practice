class CheckPermutation:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def check_permutation(self):
        word_freq = {}
        if len(self.str1) != len(self.str2):
            return False
        for i in self.str1:
            if i not in word_freq:
                word_freq[i] = 1
            word_freq[i] += 1
        for i in self.str2:
            if i not in word_freq:
                return False
            word_freq[i] -= 1

            if word_freq[i] == 0:
                del word_freq[i]

        return True


if __name__ == "__main__":
    str1 = str(input("Enter string 1: "))
    str2 = str(input("Enter string 2: "))

    c = CheckPermutation(str1, str2)
    print(c.check_permutation())

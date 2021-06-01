class PermutationCheck:
    def __init__(self, str1):
        self.str1 = str1

    def bool_permutation(self):
        dict = {}
        odd_count = 0
        for i in self.str1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for i in dict:
            if dict[i] % 2 == 1:
                odd_count += 1
        if odd_count > 1:
            return False
        if len(self.str1) % 2 == 0 and odd_count > 0:
            return False
        if len(self.str1) % 2 == 1 and odd_count > 1:
            return False

        return True


if __name__ == "__main__":
    input_str = str(input("Enter the String: "))
    a = PermutationCheck(input_str)
    print(a.bool_permutation())

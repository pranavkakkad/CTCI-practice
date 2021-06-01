class StringCompress:
    def __init__(self, str1):
        self.str1 = str1

    def compression(self):
        compr_str = []
        count = 0
        for i, j in enumerate(self.str1):
            if i != 0 and self.str1[i] != self.str1[i - 1]:
                compr_str.append(self.str1[i - 1] + str(count))
                count = 0
            count += 1

        if count > 0:
            compr_str.append(self.str1[-1] + str(count))
        print(compr_str)
        return min(self.str1, "".join(compr_str), key=len)


if __name__ == "__main__":
    str1 = str(input("Enter the string: "))
    a = StringCompress(str1)
    print(a.compression())
    print(len("helloooooooooooooooooooo"))

class UniqueString:
    def __init__(self, input_str):
        self.input_str = input_str

    def check_unique(self):
        dict = {}
        if len(self.input_str) > 128:
            return False
        for i in self.input_str:
            if i in dict:
                return False
            dict[i] = 1
        return True


if __name__ == "__main__":
    inp = str(input("Enter the string: "))
    str1 = UniqueString(inp)
    print(str1.check_unique())

import numpy as np


class RotateMatrix:
    def __init__(self, arr):
        self.arr = arr

    def perform_rotation(self):
        pass


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    col = int(input("Enter number of columns: "))
    arr = list(map(int, input("Enter value with space in between: ").split()))
    arr = np.array(arr).reshape(rows, col)
    print(arr)
    a = RotateMatrix(arr)
    print(a.perform_rotation())

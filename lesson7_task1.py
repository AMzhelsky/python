class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))


my_matrix = Matrix([[100, 200, 300, 400],
                    [1000, 2000, 3000, 4000],
                    [10000, 20000, 30000, 40000],
                    [100000, 200000, 300000, 400000]],
                   [[1000, 2000, 3000, 4000],
                    [10, 20, 30, 40],
                    [100, 200, 300, 400],
                    [1000, 2000, 3000, 4000]])

print(my_matrix.__add__())

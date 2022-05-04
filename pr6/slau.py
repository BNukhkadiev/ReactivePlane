dim = int(input('Matrix size: '))

print('Построчно введите элементы матрицы через пробел: ')
mat = []
for i in range(dim):
    s = list(map(int, input().split()))
    mat.append(s)
    assert len(s) == dim


def calc_det(matrix):
    pass

print(mat)

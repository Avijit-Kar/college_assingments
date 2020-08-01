# Avijit kumar kar(2)
# eigen value problem(2)

import numpy as np


def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]


def isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if mat[i][j] != tr[i][j]:
                return False
    return True


def checking_array(x):
    if isinstance(x, np.ndarray):
        res = x
    else:
        res = np.array(x, dtype=float)
    return res


def eigen_using_power(A, eigen_vec, accuracy=0.1):
    global eigen_val

    A = checking_array(A)
    eigen_vec = checking_array(eigen_vec)
    eigen_val = np.inf
    delta = np.inf

    while delta >= accuracy:
        eigen_vec = np.dot(A, eigen_vec)
        new_eigen_val = max(eigen_vec)

        delta = abs(eigen_val - float(new_eigen_val))

        eigen_val = new_eigen_val
        eigen_vec /= eigen_val

    print(f'eigen vector: {eigen_vec}')


input_ = input('file name: ')
try:
    A = np.loadtxt(input_, dtype=float)
except OSError:
    A = np.array(eval(input_))

X = (1, 1, 1)
print(f'given matric {A}')
if isSymmetric(A, len(X)):
    print("matic is symmetric")
    print(f'given initial eigen vec{X}')

    eigen_using_power(A, X)
    print(f'eigen value: {eigen_val}')

else:
    print("No matric is not symmetric")

"""
output:-

file name: college.txt
given matric [[1. 2. 0.]
 [2. 1. 0.]
 [0. 0. 1.]]
matic is symmetric
given initial eigen vec(1, 1, 1)
eigen vector: [1.         1.         0.11111111]
eigen value: 3.0



"""

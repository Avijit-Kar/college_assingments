#Avijit kumar kar
import numpy as np

# i=np.sqrt(-1)
a = np.array([3, 2 * 1j, 6, 7, 4, 5 * 1j, 2, 6, 3])
print('3 cross 3 matrix x is:')
x = a.reshape((3, 3))
print(x)


def Herminitian(arg):
    print(f'{arg}')
    global trans
    conj = np.conjugate(arg)
    trans = np.transpose(conj)
    print('transpose of conjugate matrix of it')
    print(f'dagger matrix: {trans}')


def checking_herm(arg1, arg2):
    if np.all(arg1 == arg2):
        print('it is herminitian matrix')
    else:
        print('it is not herminitian matrix')


print(' x matrix is:')
Herminitian(x)


print('Now the Herminitian matrix A is:')
A = 1 / 2 * (np.add(x, trans))
print('A is:')
Herminitian(A)
checking_herm(trans, A)


def Unitary(arg3):
    print('unitary matrix is:')
    q,r=np.linalg.qr(arg3)

    print(q)
Unitary(x)
"""result--------

3 cross 3 matrix x is:
[[3.+0.j 0.+2.j 6.+0.j]
 [7.+0.j 4.+0.j 0.+5.j]
 [2.+0.j 6.+0.j 3.+0.j]]
 
 x matrix is:
[[3.+0.j 0.+2.j 6.+0.j]
 [7.+0.j 4.+0.j 0.+5.j]
 [2.+0.j 6.+0.j 3.+0.j]]
 
transpose of conjugate matrix of it
dagger matrix: [[3.-0.j 7.-0.j 2.-0.j]
 [0.-2.j 4.-0.j 6.-0.j]
 [6.-0.j 0.-5.j 3.-0.j]]
 
Now the Herminitian matrix A is:
A is:
[[3. +0.j  3.5+1.j  4. +0.j ]
 [3.5-1.j  4. +0.j  3. +2.5j]
 [4. +0.j  3. -2.5j 3. +0.j ]]
 
transpose of conjugate matrix of it
dagger matrix: [[3. -0.j  3.5+1.j  4. -0.j ]
 [3.5-1.j  4. -0.j  3. +2.5j]
 [4. -0.j  3. -2.5j 3. -0.j ]]
it is herminitian matrix


unitary matrix is:
[[-0.38100038+0.j          0.3556715 -0.31417649j -0.68041382+0.40824829j]
 [-0.88900089-0.j          0.09484573+0.12448502j  0.40824829-0.13608276j]
 [-0.25400025-0.j         -0.86546731+0.03556715j -0.40824829-0.13608276j]]
 
 """






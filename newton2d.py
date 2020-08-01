# Avijit kumar kar
# Newton raphson nd (3)
import numpy as np

f = lambda x, y: (x ** 2) + (y ** 2) - 1
g = lambda x, y: (y ** 2) - (4 * x)

x1 = float(input('initial guess x: '))
y1 = float(input('initial guess y: '))


def J(x, y):
    h = 10E-10
    fx = (f((x + h), y) - f(x, y)) / h
    fy = (f(x, (y + h)) - f(x, y)) / h
    gx = (g((x + h), y) - g(x, y)) / h
    gy = (g(x, (y + h)) - g(x, y)) / h
    return np.array([[fx, fy], [gx, gy]]).reshape(2, 2)


def right_f(x, y):
    return np.array([f(x, y), g(x, y)]).reshape(2, 1)


tol = 1E-2


def root(x, y):
    while True:
        jaccobian = J(x, y)

        inverse = np.linalg.inv(jaccobian)

        sub1 = np.array([x, y]).reshape(2, 1)
        sub2 = np.dot(inverse, right_f(x, y))

        x_n, y_n = sub1 - sub2

        if abs(np.array(x_n) - np.array(x)) > tol:
            x, y = sub1 - sub2
            y = float(y_n)
            x = float(x_n)




        else:
            break
    print('roots are as follows: ')
    return np.array([x_n, y_n])


print(root(x1, y1))

"""
output:

initial guess x: 0.5
initial guess y: 0.5
roots are as follows: 
[[0.23606798]
 [0.97221699]]

"""
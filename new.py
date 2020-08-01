h = 1E-10
d_dx = lambda f: lambda x: (f(x + h) - f(x)) / h


# for single variable
def newton_rapson(f, x_n, tol=1E-10):
    f_dash = d_dx(f)
    while abs(f(x_n)) > tol:
        x_n = x_n - (f(x_n) / f_dash(x_n))
    return x_n


sqrt = lambda x: newton_rapson(lambda t: (t ** 2) - x, x / 2)

print(sqrt(1j))
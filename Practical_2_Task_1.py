"""Practical work 2, variant 1: three numerical methods."""

def f(x, y):
    return x * y**2 - x**2 + 1


def euler(x, y, h):
    return y + h * f(x, y)


def euler_cauchy(x, y, h):
    predicted = y + h * f(x, y)
    return y + (h / 2) * (f(x, y) + f(x + h, predicted))


def runge_kutta(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6


step = 0.1
values = [0.7, 0.7, 0.7]
methods = [euler, euler_cauchy, runge_kutta]

print("x        Euler        Euler-Cauchy       Runge-Kutta 4")
print(f"{4.0:.1f}   {values[0]:12.8f}   {values[1]:12.8f}   {values[2]:12.8f}")

for i in range(10):
    x = 4.0 + i * step
    for j in range(3):
        values[j] = methods[j](x, values[j], step)
    print(f"{x+step:.1f}   {values[0]:12.8f}   {values[1]:12.8f}   {values[2]:12.8f}")

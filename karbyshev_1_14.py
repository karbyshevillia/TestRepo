import math

x, y = [float(k) for k in input().split()]
p = x * y
q = math.hypot(x, y)
r = (x + y - 1) ** 2
X = 2 * p / q - r / p
print(f"{X:.3f}")
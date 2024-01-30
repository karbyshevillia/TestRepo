x, y = [float(k) for k in input().split()]
p = x ** 2 - 2 * x * y + 4 * y ** 2
q = x + 5
r = 3 * x ** 2 - y ** 2
s = y - 7
X = p / q + r / s
print(f"{X:.3f}")
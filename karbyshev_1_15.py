N = int(input())
M = abs(N)
a = M // 100
b = (M // 10) % 10
c = M % 10
p = a * b * c
q = a + b + c
print(p - q)

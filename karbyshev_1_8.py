n = int(input())
a_1 = n // 100
a_2 = (n // 10) % 10
a_3 = n % 10
p = a_1 * a_2 * a_3
print(p)
a, b, n = [int(k) for k in input().split()]
S = n * ((a * 100) + b)
s_1 = S // 100
s_2 = S % 100
print(s_1, s_2)

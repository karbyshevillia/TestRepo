def triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def obtuse(a, b, c):
    if triangle(a, b, c) == False:
        return "No triangle"
    sides = sorted([a, b, c])[::-1]
    return sides[0] ** 2 > sides[1] ** 2 + sides[2] ** 2

############################### MAIN PROGRAM ###################################

a, b, c = [float(d) for d in input().split()]

print(triangle(a, b, c), obtuse(a, b, c))

# 12 minutes
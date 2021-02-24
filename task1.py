n = int(input())
base = []

while n > 0:
    base.append(input())
    base.append(float(input()))
    base.append(float(input()))
    base.append(float(input()))
    n -= 1

a = base.index(str(input()))
sm = (base[a+1] + base[a+2] + base[a+3])/3
print(sm)


A = input()
cd = [0, 0]
for i in range(0, len(A)):
    if A[i] == "R":
        cd[1] += 1
    elif A[i] == "L":
        cd[1] -= 1
    elif A[i] == "U":
        cd[0] += 1
    elif A[i] == "D":
        cd[0] -= 1
    else:
        print("not match letter")
if cd[0] == cd[1] == 0:
    print("True")
else:
    print("False")

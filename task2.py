
A = input().split()
B = input().split()
dr = {}

for i in range(0, len(A)):

    if i < len(B):
        dr[A[i]] = B[i]
    else:
        dr[A[i]] = None
print(dr)

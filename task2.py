
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dr = {}

for i in range(len(A)):

    if i < len(B):
        dr[A[i]] = B[i]
    else:
        dr[A[i]] = None
print(dr)

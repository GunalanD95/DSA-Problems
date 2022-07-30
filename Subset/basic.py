A = "dfbkjijgbbiihbmmt"
B = "bit"

A = list(A)
N = len(A)
rng = 1 << N
print(A,"length",N,"rng",rng)

# def checkbit(n,j):
#     if (1 << j) & n:
#         return 1
#     return 0

# for i in range(rng):
#     cur = []
#     for j in range(N):
#         if checkbit(i,j):
#             cur.append(A[j])
#     print("subarr",cur)
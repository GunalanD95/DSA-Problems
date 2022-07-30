mat = [[1,2,3],
       [4,5,6]]
       
rows = len(mat)
cols = len(mat[0])

pf = [[0]*cols for i in range(rows)]

# row wise pf
for i in range(rows):
    prev = mat[i][0]
    pf[i][0] = mat[i][0]
    for j in range(1,cols):
        pf[i][j] = prev + mat[i][j]
        prev = pf[i][j]
        
print("ROW-PF",pf)

# col wise pf
for j in range(cols):
    prev = pf[0][j]
    for i in range(1,rows):
        pf[i][j] = prev + pf[i][j]
        prev = pf[i][j]
        
print("COL-PF",pf)
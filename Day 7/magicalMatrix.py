#Magical matrix for odd sizes like 3X3,5X5,etc
#For n=3
# [2, 7, 6]
# [9, 5, 1]
# [4, 3, 8]
n = int(input("Enter size of matrix: "))
mat = [[0]*n for k in range(n)]

def gen(i,j,num):
    if num > n*n:
        return mat
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
        if mat[i][j]:
            return gen(i+1,j-2,num)
    mat[i][j]=num
    return gen(i-1,j+1,num+1)


m = gen(n//2,n-1,1)
for i in m:
    print(i)




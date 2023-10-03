def TowerOfHanoi(n):
    if n==1:
        return 1
    else:
        return 2*TowerOfHanoi(n-1)+1

n=int(input())
print(TowerOfHanoi(n))
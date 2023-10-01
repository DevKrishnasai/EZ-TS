# Diffrenet star patterns
n = int(input())
for i in range(n):
    print("* "*(i+1))

print()

# n = int(input())
for i in range(n):
    print(" "*(n-i-1),end="")
    print("* "*(i+1))

print()

# n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

print()

# n = int(input())
for i in range(n):
    print(" "*(n-i-1),end="")
    print("* "*(i+1))

for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
































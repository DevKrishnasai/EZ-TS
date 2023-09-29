#here we check the position of 1 after the operation if it is in the given position then true else false.
# 15 - 1111
# pos - 3

# then 1 should be shifted pos-1(2) times
# 0001 ->  0100

# 1111
# 0100
# ----
# 0100
# ----
# at pos 3 there is 1 => true

n = int(input())
pos = int(input())
s= 1<<pos-1     #shifthing to left
res = n&s

print(res)

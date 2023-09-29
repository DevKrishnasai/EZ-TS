n = 7
for i in reversed(range(15)):  #for 16 bit range is 15
    if 1<<i & n:
        print(1 ,end=" ")
    else:
        print(0 ,end=" ")


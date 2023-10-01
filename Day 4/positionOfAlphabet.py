#position of the character in the alphabetic order
a = input()
if a.isupper():
    print(ord(a)-ord("A")+1)
else:
    print(ord(a)-ord("a")+1)

#jump to another character
a = input()
x = int(input())
if a.isupper():
    if ord(a)+x > ord("Z"):
        print(chr(ord(a)+x-26))
    else:
        print(chr(ord(a)+x))
else:
    if ord(a)+x > ord("z"):
        print(chr(ord(a)+x-26))
    else:
        print(chr(ord(a)+x))



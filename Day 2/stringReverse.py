#Reversing a string without distrubing special characters and spaces

n = input()
l = []
s = ""
temp_n = n.lower()
for i in range(len(n)):
    if n[i] == ' ' or n[i] in '[@_!#$%^&*()<>?/\|}{~:],.':
        l.append((i, n[i]))
    else:
        s += n[i]

s = list(s)
s1 = ""
prev = 0

for i in l:
    for j in range(prev, i[0]):
        s1 += s.pop()
    s1 += i[1]
    prev = i[0] + 1

print(s1)

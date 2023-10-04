

#Method 1
def printParenthesis(str, pos, n,open, close):
	print(str,pos,n,open,close)
	if(close == n):
		for i in str:
			print(i, end="")
		print()
		return
	else:
		if(open > close):
			str[pos] = ')'
			printParenthesis(str, pos + 1, n,open, close + 1)
		if(open < n):
			str[pos] = '('
			printParenthesis(str, pos + 1, n,open + 1, close)


n = 3
str = [""] * 2 * n
printParenthesis(str, 0,n,0,0)


#Method 1 simplified version
def par(s,l,r):
    if len(s)==n*2:
        res.append(s)
    else:
        if r<l:
            par(s+")",l,r+1)
        if l<n:
            par(s+"(",l+1,r)

n = int(input())
res = []
par("",0,0)
print(res)


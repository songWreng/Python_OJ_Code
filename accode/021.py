# coding=utf-8

def Solve(cur, curLeft, curRight, pre, preLeft, preRight):
	if curLeft == curRight and preLeft == preRight:
		print(cur[curLeft], end=" ")
	else:
		root = cur[curLeft:curRight+1].index(pre[preLeft]) + curLeft
		if curLeft <= root - 1:
			Solve(cur, curLeft, root - 1, 
				  pre, preLeft + 1, preLeft + root - curLeft)
		if root + 1 <= curRight:
			Solve(cur, root + 1, curRight, 
				  pre, preLeft + root - curLeft + 1, preRight)
		print(cur[root], end=" ")

def main():
	pre = [b for b in input().split()]
	cur = [b for b in input().split()]
	Solve(cur, 0, len(cur) - 1, pre, 0, len(pre) - 1)
	print()

main()

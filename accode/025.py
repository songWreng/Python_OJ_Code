# coding=ANSI
'''
递归的方式
判断一棵树是否为合法的树，前提是：
	两棵子树都是合法的树
	判断根结点与左子树、右子树的关系：
		如果左子树和右子树均为空，则放回根结点
		如果左子树为空，右子树不为空，则比较根结点和右子树(min)，如果最小的是根，则放回根结点
		如果左子树不为空，右子树为空，则比较根结点和左子树(min)，如果最小的是左结点，则返回左子树
		如果左子树和右子树均不为空，则比较根与左子树、根和右子树，如果均满足上述关系，则返回左子树
判断一个结点是否为空，存在两种情况：
	序号超过了边界值
	序号没有超过边界值，但是其对应的值是一个空树标记。
为空的子树返回的值应该是一个很大的值
'''
def helpsolve(p, cur):
	if cur < len(p) and p[cur] != '#':
		left = 2*cur + 1
		right = 2*cur + 2
		leftres = (left < len(p) and p[left] != '#')
		rightres = (right < len(p) and p[right] != '#')
		if leftres == True and rightres == False:
			leftmin = helpsolve(p, left)
			if leftmin != -1 and leftmin < p[cur]: return leftmin
			else: return -1
		elif leftres == False and rightres == True:
			rightmin = helpsolve(p, right)
			if rightmin != -1 and rightmin > p[cur]: return p[cur]
			else: return -1
		elif leftres == True and rightres == True:
			leftmin = helpsolve(p, left)
			rightmin = helpsolve(p, right)
			if leftmin == -1 or rightmin == -1: return -1
			if leftmin < p[cur] and p[cur] < rightmin: return leftmin
			else: return -1
		elif leftres == False and rightres == False:
			return p[cur]
	
	pass
	
def main():
	p = input().split()
	for i in range(len(p)):
		if p[i] != '#': p[i] = int(p[i])
	print(helpsolve(p, 0) != -1)

main()



'''
10
12 13
24
'''


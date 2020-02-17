# coding=utf-8
#def merge_sort(list1):
    #if len(list1) <= 1:
        #return list1
    #num = len(list1) // 2
    #left = merge_sort(list1[:num])
    #right = merge_sort(list1[num:])
    #return merge(left,right)
  
#def merge(left,right): # x
    #l, r = 0, 0
    #result = []
    #while l < len(left) and r < len(right):
        #if left[l] <= right[r]:
           #result.append(left[l])
           #l += 1
        #else:
           #result.append(right[r]) # pin xie
           #r += 1
    #result += left[l:]
    #result += right[r:]
    #return result
  
#num = int(input())
#for i in range (num):
    #li = [int (k) for k in list(input().split())]
    #sorted_li = merge_sort(li)
    #print(sorted_li)
# coding=utf-8
#def quick_sort(list1, start, end):
	#if start >= end:
		#return
	#mid = list1[start]
	#left = start
	#right = end
	#while left < right:
		#### 从这里开始
		## 增加if
		#while left < right and list1[right] >= mid:
			#right -= 1
		#if left < right:
			#list1[left] = list1[right]
			#left += 1
			#while left < right and list1[left] < mid:
				#left += 1
			#if left < right:	
				#list1[right] = list1[left]	
				#right -= 1
		#### 到这里结束


	#list1[left] = mid
	#quick_sort(list1, start, left-1)		
	#quick_sort(list1, left+1, end)
		
#num = int(input())
#for i in range (num): # error
      #li = [int(k) for k in list(input().split())] # error
      #quick_sort(li, 0, len(li)-1)
      #print(li)

def FindNum(p, a, b, num):
	pass
	for i in range(a, b + 1):
		if num == p[i]:
			return i
	return -1


def Fun(q, ql, qr, p, pl, pr):
	if (ql == qr and pl == pr):
		print(q[ql],end=" ")
	else:
		root = FindNum(q, ql, qr, p[pr])
		print(q[root], end = " ")
		if ql <= root - 1:
			Fun(q, ql, root - 1, p, pl, pl + root - 1 - ql)
		if root + 1 <= qr:
			Fun(q, root + 1, qr, p, pr - qr + root, pr - 1)
		
def test():
	#q = [3,1,4,0,2]
	#p = [3,4,1,2,0]
	#a = [0,1,3,4,2] 

	#p = [6,7,5,4,3,1,2,0]

	#q = [1,3,4,6,5,7,0,2]
	#a = [0,1,3,4,5,6,7,2]

	#q = [6,5,7,4,3,1]
	#p = [6,7,5,4,3,1]

	q = [7,3,8,1,4,0,9,5,10,2,6]
	p = [7,8,3,4,1,9,10,5,6,2,0]
	print("后序：")	
	print(q)
	print("中序：")
	print(p)
	print("先序：")
	Fun(q, 0, len(q)-1, p, 0, len(p)-1)
	print()

# q 是中序遍历，p是先序
def Fund(q, ql, qr, p, pl, pr):
	if ql == qr and pl == pr:
		print(q[ql], end=" ")
	else:
		root = FindNum(q, ql, qr, p[pl])
		
		if ql <= root - 1:
			#Fun(q, ql, root - 1, p, pl + 1, pl + 1 + root - 1 - ql)
			Fund(q, ql, root - 1, p, pl + 1, pl + root - ql)
		if root + 1 <= qr:
			#Fund(q, root + 1, qr, p, pl + root - 1 - ql + 1 + 1, pr)
			Fund(q, root + 1, qr, p, pl + root - ql + 1, pr)
		print(q[root], end=" ")

def test2():
	# p 是中序， q 是前序
	#p = [3,1,4,0,2]
	#q = [0,1,3,4,2]
	
	#p = [1,3,4,6,5,7,0,2]
	#q = [0,1,3,4,5,6,7,2]
	
	p = [7,3,8,1,4,0,9,5,10,2,6]
	q = [0,1,3,7,8,4,2,5,9,10,6]
	Fund(p, 0,len(p) - 1, q, 0, len(q) - 1)
	print()

if __name__ == "__main__":
	#test()
	#test2()
	
	datas = [
				[
					[0,1,3,7,8,4,2,5,9,10,6],
					[7,3,8,1,4,0,9,5,10,2,6],
					[7,8,3,4,1,9,10,5,6,2,0]],
				[
					[0,1,2,3,4],
					[3,2,4,1,0],
					[3,4,2,1,0]],
				[
					[0,1,2,3,4],
					[0,1,3,2,4],
					[3,4,2,1,0]],
				[
					[0],[0],[0]],
				[
					[0,1,3,4,6,2,5,7],
					[3,1,6,4,0,2,7,5],
					[3,6,4,1,7,5,2,0]]

			
			]
	s = ["前序: ", "中序: ", "后序: "]
	for i in range(len(datas)):
		print("Case", i + 1, ":")
		for j in range(3):
			print(s[j], datas[i][j])
	
	for i in range(len(datas)):
		print("测试1：")
		print("post =", datas[i][2])
		print(" cur =", datas[i][1])
		print(" pre =", end=" ")
		Fun(datas[i][1], 0, len(datas[i][1])-1, 
			datas[i][2], 0, len(datas[i][2])-1)
		print()
		print("测试2：")
		print(" pre =", datas[i][0])
		print(" cur =", datas[i][1])
		print("post =", end=" ")
		Fund(datas[i][1], 0, len(datas[i][1])-1,
			 datas[i][0], 0, len(datas[i][0])-1)
		print()	
	


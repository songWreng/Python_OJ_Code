# coding=ANSI
# Hash�����ɾ��
def solve14():
	n = int(input())
	p = [int(b) for b in input().split()]
	
	h = []
	for i in range(n):
		h.append([None])

	# ����Hash��
	for b in p:
		i = hashf(b, n)
		if h[i] == [None]:
			h[i][0] = b
		else:
			if not b in h[i]:
				h[i].append(b)

	# ����Ԫ��
	tmp = int(input())
	while tmp > 0:
		nums = int(input())
		i = hashf(nums, n)
		if h[i] == [None]:
			h[i][0] = nums
		else:
			if not nums in h[i]:
				h[i].append(nums)
		tmp -= 1
	
	# ɾ��Ԫ��
	tmp = int(input())
	while tmp > 0:
		nums = int(input())
		i = hashf(nums, n)
		if nums in h[i]:
			del h[i][h[i].index(nums)]
		else:
			print("Delete Error")
		if h[i] == []:
			h[i] = [None]
		tmp -= 1

	# ����Ԫ��
	tmp = int(input())
	while tmp > 0:
		nums = int(input())
		i = hashf(nums, n)
		print(nums in h[i])
		tmp -= 1

def hashf(key, n):
	return (key % n)
      
solve14()
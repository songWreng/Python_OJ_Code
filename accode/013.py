# coding=ANSI
'''
��Ŀ������
����һ��������N������N�Ķ�����������������1֮�������롣�������������������1���򷵻�0
�������ڵ�1�ľ���Ϊ1����101��1�ľ���Ϊ2����������
������
22 => 2
 8 => 0
�⣺
22 = 10110��8 = 1000
'''
def solve13(n):
	maxi = cur = 0
	mask = 0
	while n != 0:
		if n % 2 == 1:
			if mask != 0: cur += 1
			maxi = max(maxi, cur)
			cur = 0
			mask = 1
		elif n % 2 == 0 and mask == 1:
			cur += 1
		n //= 2
	print(maxi)
	pass
    
solve13(int(input()))  
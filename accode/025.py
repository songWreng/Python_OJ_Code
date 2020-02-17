# coding=ANSI
'''
�ݹ�ķ�ʽ
�ж�һ�����Ƿ�Ϊ�Ϸ�������ǰ���ǣ�
	�����������ǺϷ�����
	�жϸ���������������������Ĺ�ϵ��
		�������������������Ϊ�գ���Żظ����
		���������Ϊ�գ���������Ϊ�գ���Ƚϸ�����������(min)�������С���Ǹ�����Żظ����
		�����������Ϊ�գ�������Ϊ�գ���Ƚϸ�����������(min)�������С�������㣬�򷵻�������
		���������������������Ϊ�գ���Ƚϸ��������������������������������������ϵ���򷵻�������
�ж�һ������Ƿ�Ϊ�գ��������������
	��ų����˱߽�ֵ
	���û�г����߽�ֵ���������Ӧ��ֵ��һ��������ǡ�
Ϊ�յ��������ص�ֵӦ����һ���ܴ��ֵ
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


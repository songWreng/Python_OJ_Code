# coding=ANSI
'''
˼·��
	���ݲ��Ҷ��������ص㣬����Ψһȷ��һ������Ҳ����˵���ǵ���ȫ�������������ͬ��
���Կ��Կ��Ǽ���ԭ���е���ȫ����������ţ�����������������У�
	�����ͬһ�����ı�Ҫ�����ǣ����еĳ�����ͬ�����Ȳ�ͬһ������False��
	�������������е���ȫ����������ţ��������������
		ĳ��������Ų���ԭ�����еķ�Χ��
		ĳ����Ŷ�Ӧ��ֵ��ͬ��
����������������ж�ΪFalse��
'''
def solve24():
	N = int(input())
	p = [int(b) for b in input()]
	dp = {0:p[0]}
	for a in p[1:]:
		i = 0
		while i in dp:
			if a < dp[i]:
				i = 2*i + 1
			elif a > dp[i]:
				i = 2*i + 2
		dp[i] = a

	while N > 0:
		q = [int(b) for b in input()]
		if len(q) == len(p):
			flag = True
			dq = {0:q[0]}
			for a in q[1:]:
				i = 0
				while i in dq:
					if a < dq[i]:
						i = 2*i + 1
					elif a > dq[i]:
						i = 2*i + 2
				dq[i] = a

				if (i not in dp) or dp[i] != a:
					flag = False
					break
		else:
			flag = False

		if flag == True:
			print("YES")
		else:
			print("NO")
		N -= 1

	pass # end function

solve24()


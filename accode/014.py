# coding=ANSI
# Hash��Ӧ��: ��ͬһ��ֱ���ϵĵ������
h = [None] * 10 # Hash��
mah = [0] * 10  # ��¼�±��ͻ�ĸ���
n = int(input())
while n > 0:
	p = [int(b) for b in input().split()]
	k = p[1] // p[0] # б�ʹؼ���
	i = k % 10
	while h[i] != None and h[i] != k:
		i += 1;
		if i >= 10 : i = 0
	if h[i] == None:
		h[i] = k
	mah[i] += 1 # ����+1
	n -= 1

print(max(mah))




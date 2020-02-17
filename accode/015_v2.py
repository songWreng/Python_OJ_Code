'''
输入：
字符串：宝石的种类，不会重复
字符串：我有的石头

输出:
宝石的数量

注意：
存在大小写
Hash的大小不超过10
'''
class Hash():
	def __init__(self, s):
		self.HashSize = s
		self.HashTable = [None]*s

	def Insert(self, v):
		i =  v % self.HashSize
		while self.HashTable[i] != None:
			i = (i + 1) % self.HashSize
		self.HashTable[i] = v
		return i

	def Find(self, v):
		i = v % self.HashSize
		while self.HashTable[i] != None and self.HashTable[i] != v:
			i =  (i + 1) % self.HashSize
		if self.HashTable[i] == v:
			return i
		else:
			return -1

def solve():
	h = Hash(10)
	for a in input():
		h.Insert(ord(a))
	cnt = 0
	for a  in input():
		if h.Find(ord(a)) != -1:
			cnt += 1
	print(cnt)

solve()





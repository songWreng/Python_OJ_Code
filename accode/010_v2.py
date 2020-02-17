'''
除留余数法，链冲突，保证不会溢出，重复的元素只保存一个
size 是散列表的大小
数据，建立散列
n
n个插入元素(无输出)
m
m个删除元素(删除元素不在散列表中，输出Delete Error)
r
r个查找元素(在,True，不在,False)
'''
from collections import deque
class HashTable():
	def __init__(self, s):
		self.HashSize = s
		self.Table = [None]*s
	def Insert(self, v):
		i = v % self.HashSize
		if self.Table[i] == None:
			self.Table[i] = deque([v])
		else:
			if v not in self.Table[i]:
				self.Table[i].append(v)
		return i		
	def Find(self, v):
		i = v % self.HashSize
		if self.Table[i] != None and v in self.Table[i]:
			return i
		return -1

	def Delete(self, v):
		i = v % self.HashSize
		if self.Table[i] != None and v in self.Table[i]:
			del self.Table[i][self.Table[i].index(v)]
			if len(self.Table[i]) == 0:
				self.Table[i] = None
			return i
		else:
			return -1	
	def PrintInf(self):
		print('[i]: v')
		for i in range(self.HashSize):
			print("[%d]:" % i, end=" ")
			print(self.Table[i])

def solve():
	h = HashTable(int(input()))
	for i in [int(b) for b in input().split()]:
		h.Insert(i)
	for i in range(int(input())):
		h.Insert(int(input()))
	for i in range(int(input())):
		if h.Delete(int(input())) == -1: print("Delete Error")
	for i in range(int(input())):
		if h.Find(int(input())) == -1:
			print("False")
		else:
			print("True")

def test01():
	h = HashTable(5)
	print("插入操作:")
	p = [4,2,3,2]
	for a in p:
		h.Insert(a)
	h.PrintInf()
	print("删除操作:")
	p = [2,0]
	for a in p:
		if h.Delete(a) == -1:
			print("Can't find", a, "/Delete Error")
		else:
			print("Delete", a)
	h.PrintInf()

	h.Insert(1)
	h.Insert(10)
	p = [10, 20, 4, 3]
	for a in p:
		if h.Find(a) == -1:
			print("Can't find", a)
		else:
			print("Yes,",a, "in Hash")	
	h.PrintInf()

def main():
	test01()
	# solve()
main()


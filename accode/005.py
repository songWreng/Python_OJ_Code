# coding=ANSI
# øÏÀŸ≈≈–Ú
def quickSort(p):
	helpquickSort(p, 0, len(p) - 1)
	
def helpquickSort(p, left, right):
	if left < right:
		a = Mask(p, left, right)
		helpquickSort(p, left, a - 1)
		helpquickSort(p, a + 1, right)
          
def Mask(p, left, right):
	mid = (left + right) // 2
	val = p[mid]
	p[mid] = p[left]
	i = left; j = right
	while i < j:
		while p[j] >= val and i < j: j -= 1
		if j > i:
			p[i] = p[j]
			i += 1
			while p[i] <= val and i < j: i += 1
			if j > i:
				p[j] = p[i]
				j -= 1
	p[i] = val
	return i

def main():
	n = int(input())
	while n > 0:
		p = [int(b) for b in input().split()]
		quickSort(p)
		print(p)
		n -= 1
          
          
main()

import random


class BinarySearch:

	def __init__(self, arry):
		self.arry = arry

	def find(self, n):
		l,r = 0, len(self.arry)-1
		steps = 0

		while l<=r:
			steps += 1
			m = l + ((r-l)//2)  
			if self.arry[m]==n:          
				print ("FOUND IT, steps:=",steps, 'arry len:=',len(self.arry))
				return True

			if self.arry[m]>n:
				r = m - 1
			elif self.arry[m]<n:
				l = m + 1			
 
		print ("DID NOT FIND",n,"steps:=",steps, 'arry len:=',len(self.arry))
		print (self.arry)
		return False


def test1():
	print ("test 1")
	arry_len = 300
	arry = [random.randint(0, arry_len*2) for _ in range(0,arry_len)]
	arry.sort() #nlogn	
	bs = BinarySearch(arry)
	f = bs.find(79)
	print ('found it',f)


def test2():
	print ("test 2")	
	arry = [7,12,13,16,22,52,55,56,60,61,62,66,73,78,91,99,100,101]	
	bs = BinarySearch(arry)
	f = bs.find(16)
	print ('found it',f)


def test3():
	print ("test 3")
	arry_len = 3000000
	arry = [random.randint(0, arry_len*2) for _ in range(0,arry_len)]
	arry.sort() #nlogn	
	bs = BinarySearch(arry)
	f = bs.find(arry[91])
	print ('found it',f)
	
if __name__=='__main__':
	print ("Start...")

	test1()
	print ("*"*32)
	test2()
	print ("*"*32)
	test3()

	print ("END!")


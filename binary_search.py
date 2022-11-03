import random


class BinarySearch:

	def __init__(self, arry):
		self.arry = arry

	def find(self, n):
		l,r = 0, len(self.arry)-1
		counter = 0

		while l<r:
			counter += 1
			m = l + ((r-l)//2)  
			if arry[m]==n:          
				print ("FOUND IT, counter:=",counter)
				return True
			if arry[m]>n:
				r = m - 1
			elif arry[m]<n:
				l = m + 1			
 
		print ("DID NOT FIND IT, countery:=",counter)
		return False


if __name__=='__main__':
	print ("Start...")

	arry_len = 300
	arry = [random.randint(0, arry_len*2) for _ in range(0,arry_len)]
	arry.sort() #nlogn	
	bs = BinarySearch(arry)
	f = bs.find(79)
	print ('found it',f)

	print ("END!")

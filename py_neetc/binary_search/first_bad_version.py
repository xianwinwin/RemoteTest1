'''
https://leetcode.com/problems/first-bad-version/description/
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after 
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number 
of calls to the API.
'''

def isBadVersion(v):
    if v<=3:
        return False
    return True

class Solution:

    def firstBadVersion(self, n: int) -> int:
        
        if n<=0:
            return -1

        my_version = n
        left,right = 0, n
        
        while left<right:
            mid = left + (right-left)//2
            print ("left:=",left,"right:=",right,'mid:=',mid)

            if mid==left or mid==right:
                break 
            if isBadVersion(mid):
                right = mid 
            else:
                left = mid

        return mid+1 
            


        
        


if __name__=='__main__':
    print ('start...')

    s = Solution()
    res = s.firstBadVersion(n=5)
    print (res)
    print ("END ")
 
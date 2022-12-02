#https://leetcode.com/problems/container-with-most-water/

class Solution:

    def maxArea(self, height) -> int:
        l,r = 0, len(height)-1
        max_area = 0
        while l<r:
            h_left = height[l]
            h_right = height[r]
            distance = r-l

            area = min(h_left,h_right) * distance
            max_area = max(max_area,area)

            #move left or right? 
            if h_left > h_right:
                r-=1
            else:
                l+=1
            
        return max_area



if __name__=='__main__':
    print ("Start...")
    height= [1,8,6,2,5,4,8,3,7]
    s = Solution()
    r = s.maxArea(height)
    print (r)
    print ("END")
      
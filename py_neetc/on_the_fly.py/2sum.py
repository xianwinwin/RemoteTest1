from typing import List

class Solution: 
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # List to store results
        result = []
        # Dictionary to store the difference and its index
        index_map = {}
        # Loop for each element
        for i, n in enumerate(nums):
            # Difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        return result


if __name__=='__main__':
    nums = [2,4,5,7,11,15] 
    target = 9
    s = Solution()
    r = s.twoSum(nums,target)
    print ("r:=",r)

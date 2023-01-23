''' 
https://leetcode.com/problems/plates-between-candles/description/
There is a long table with a line of plates and candles arranged on top of it. 
You are given a 0-indexed string s consisting of characters '*' and '|' only, where a
 '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] 
denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the 
number of plates between candles that are in the substring. A plate is considered between 
candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". 
The number of plates between candles in this substring is 2, as each of the two plates 
has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.
 
'''

class Solution:

    def platesBetweenCandles(self, s, queries):
                
        def search(target):
            #user binary search (logn) to get nearest result
            l,r =0, len(cache)-1
            mid = -1
            while l<=r:
                mid = l + (r-l)//2
                mid_v = cache[mid][0]
                if mid_v==target:
                    return mid
                if target>mid_v:
                    l = mid+1
                else:
                    r= mid-1
            
            if mid==-1:
                return None

            return mid

        def adjustment(index, target, position_req):
            if index==-1:
                return -1
            
            cache_target = cache[index][0]
            if cache_target==target:
                return index
            
            if position_req=='before':
                if index==0:
                    return index
                if cache_target>target:
                    return index-1
                return index
            
            if position_req=='after':
                if index==len(cache)-1:
                    return index
                if cache_target+cache[index][1]<=target:
                    return index
                if cache_target<target:
                    return index+1
                return index

                

        def cache_stars():
            
            #trim left
            left = 0
            while left<len(s):
                if s[left]=="|":
                    break
                left+=1
            
            #trim right
            right = len(s)-1
            while right>=0:
                if s[right]=='|':
                    break
                right-=1
             
            l,r = left, left
            while l<=r<right:
                stars = 0
                while s[r]=='*':
                    stars+=1
                    r+=1
                if stars>0:
                    cache.append([l,stars])                    
                r+=1
                l=r

        cache = [] ##[ [lcoation:num_stars], [],[] ]    
        cache_stars()
        res = []

        for subq in queries:
            qf = subq[0]
            qt = subq[1]+1 #inclusive
            
            position = search(qf)
            cf = adjustment(position,qf,'after')

            position = search(qt)
            ct = adjustment(position,qt, 'before')

            stars = 0
            if cf==ct:
                if cache[cf][0]>=qf and qt>cache[ct][0]+cache[ct][1]:
                    stars+=cache[cf][1]
                    res.append(stars)
                else:
                    res.append(0)
            else:
                for i in cache[cf:ct]:
                    stars+=i[1]                    
                print ("counted",stars,'stars; from ',cf,'to',ct,'[',qf,'-->',qt,']')
                
                res.append(stars)

        return res

if __name__=='__main__':
    print ('start...')

    my_str = "**|**|***|"
    queries = [[2,5],[5,9]]

    #my_str = "***|**|*****|**||**|*"
    #queries = [[1,17],[2,10]]

    #my_str = "***|**|*****|**||**|*"
    #queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

    my_str = "*|*||||**|||||||*||*||*||**|*|*||*"
    queries =[[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]

    #my_str = "**|**|***|"
    #queries = [[2,5],[5,9]]


    s = Solution()
    res = s.platesBetweenCandles(my_str,queries)
    print (res)
    print ("END ")
 
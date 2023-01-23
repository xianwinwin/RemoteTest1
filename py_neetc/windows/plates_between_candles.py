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

        def query_stars(query,f,t):
            
            #trim left
            tl=0
            while tl<len(query) and query[tl] != '|':
                tl+=1

            tr=len(query)-1
            while tr>=0 and query[tr]!='|':
                tr-=1

            query = query[tl:tr+1]
            if query and (query[0]!='|' or query[-1]!='|'):
                return 0

            #count stars
            stars=0
            sub_stars = 0
            l,r = 0,0
            while l<len(query) and r<len(query):
                db_stars = cache.get(tl+f+l,None)
                if db_stars:
                    stars+=db_stars
                    l = l + db_stars
                    r=l
                else:
                    while query[r]=='*':
                        stars+=1
                        sub_stars+=1
                        r+=1
                        cache[tl+f+l]=sub_stars
                    r+=1
                    l=r
                    sub_stars=0
                
            return stars

        res = []
        cache = {}
        for sub in queries: #f=from; t=to
            f = sub[0]
            t = sub[1]+1 #inclusive

            query_str = s[f:t]

            res.append(query_stars(query_str,f,t))

        return res

if __name__=='__main__':
    print ('start...')

    my_str = "**|**|***|"
    queries = [[2,5],[5,9]]

    my_str = "***|**|*****|**||**|*"
    queries = [[1,17],[2,10]]


    s = Solution()
    res = s.platesBetweenCandles(my_str,queries)
    print (res)
    print ("END ")
 
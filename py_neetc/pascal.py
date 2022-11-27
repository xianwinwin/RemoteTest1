

class Solution:

    def pascal(self, n):
        res = []
        first_row = [1]
        res.append(first_row)

        for i in range(1,n+1):
            prev = res[i-1]
            
            new_line = []
            for j,k in zip(prev,prev[1:]):
                new_line.append(j+k)

            row = [1] + new_line + [1]
            res.append(row)

        return res


if __name__=='__main__':
    print ('start...')

    s = Solution()
    n=6
    res = s.pascal(n)
    for r in res:
        print (r)

    print ("END ")

'''
        [1]
       [1,1]
      [1,2,1]
     [1,3,3,1]
'''
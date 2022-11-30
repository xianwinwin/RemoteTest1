#https://leetcode.com/problems/binary-watch/

class Solution:

    def readBinaryWatch(self, turnedOn):

        if turnedOn==0:
            return ['0:00']


        def get_binary(decimal, binary_res):
            
            if decimal==0:
                return []

            n = decimal // 2
            q = decimal % 2
            get_binary(n, binary_res)
            binary_res.append(q)
            return binary_res
                
        res = []
        for h in range(0,12):            
            hb = get_binary(h,[])
            for m in range(0,60):
                mb = get_binary(m,[])
                
                time_binary = hb + mb
                if sum(time_binary)==turnedOn:
                    str_m = str(m)
                    if len(str_m)==1:
                        str_m='0'+str_m
                    res.append(str(h)+":"+str_m)


        return sorted(res)

if __name__=='__main__':
    print ("Start...")

    turnedOn = 1
    s = Solution()
    res = s.readBinaryWatch(turnedOn) 
    print (res)

    print ("END!")
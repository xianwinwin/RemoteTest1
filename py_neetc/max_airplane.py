
class Solution:

    def get_max_flights(self, flights):
        starts = sorted([f[0] for f in flights])
        ends = sorted([f[1] for f in flights])

        max_flights = 0
        counter = 1
        s_ptr = 1
        e_ptr = 0
        while s_ptr<=len(starts)-1:
            if starts[s_ptr]<ends[e_ptr]:
                counter+=1
                max_flights = max(max_flights,counter)
                s_ptr+=1
            else:
                counter-=1
                e_ptr+=1

        return max_flights

if __name__=='__main__':
    print ("Start")
    flights = [(4,9),(2,5),(17,20),(10,21),(9,18)]
    flights = [(1,2),(3,5),(6,10),(11,20),(4,8),(1,30),(4,6)]

    s = Solution()
    maxf = s.get_max_flights(flights)
    print ("max flights:=",maxf)
    print ("END")
#https://leetcode.com/problems/single-threaded-cpu/

'''
incomplete
'''
import heapq

class Solution:
    def getOrder(self, tasks):

        if not tasks:
            return []

        min_heap = []

        for i, task in enumerate(tasks):
            task.append(i)
            heapq.heappush(min_heap,task)
        
        res = []
        tasks.sort(key = lambda x: x[0])
        t = tasks[0][0]    
        while t<=tasks[-1][0] or min_heap:
            
            candidates = []
            next_time = -1
            while min_heap:
                my_task = heapq.heappop(min_heap)
                if my_task[0]<=t:
                    candidates.append(my_task)
                    next_time = my_task[1]
                else:
                    t = t+next_time
                    heapq.heappush(min_heap,my_task)
                    break
            
            #get min task to process in candidates
            if not candidates:
                return res
            
            candidates.sort(key=lambda x: (x[1],x[2]))
            process_task = candidates[0]
            res.append(process_task[2])
            
            if len(candidates)>1:
                for i in candidates[1:]:
                    heapq.heappush(min_heap,i)

        return res


if __name__=='__main__':
    print ("start...")
    
    #tasks[i] = [enqueueTimei, processingTimei]
    #tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    #tasks = [[1,2],[2,4],[3,2],[4,1]]
    tasks =[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
    tasks = [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]
    s = Solution()
    r = s.getOrder(tasks)
    print ('r:=',r)
    print ("END ")
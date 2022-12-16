from collections import defaultdict
#https://leetcode.com/problems/course-schedule-ii/

'''
210. Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course 
bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites):

        adj = defaultdict(list) #K=course V = [ pre_req, pre_req ]
        courses = set()
        for item in prerequisites:
            pre_req = item[0]
            course  = item[1]
            adj[course].append(pre_req)
            courses.add(course)
            courses.add(pre_req)

        stack = []
        visited = set()
        cycle = []

        #get to the last course that has no pre-req and add to the stack and then add the course that was K in the adj
        def dfs(course):
            if course in visited:
                return

            pre_reqs = adj.get(course, None)
            if not pre_reqs:
                stack.append(course)
                visited.add(course)
                return 
            
            for c in pre_reqs:
                dfs(c)
                if set(pre_reqs).issubset(visited):
                    stack.append(course) #add the K to the stack
                    visited.add(course)
                return 

        #itearate all courses 
        while len(visited)!=len(courses):
            for c in courses:
                dfs(c)

        res = list(reversed(stack))
        for i in range(len(res),numCourses):
            res.append(i)
        return res
    
if __name__=='__main__':
    print ("START...")

    #numCourses = 4
    #prerequisites = [[1,0],[2,0],[3,1],[3,2]]


    numCourses = 13
    prerequisites = [[0,1],[1,0]]

    s = Solution()
    res = s.findOrder(numCourses, prerequisites)
    print ('res:=',res)

    print ("END")
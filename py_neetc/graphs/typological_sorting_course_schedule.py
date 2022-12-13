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

        courses = set()
        adj = defaultdict(list)
        for p in prerequisites:
            course = p[0]
            pre_req = p[1]
            adj[course].append(pre_req)
            courses.add(course)
            courses.add(pre_req)


        def dfs(course):
            if course in cycle:
                return False
            
            visited.add(course)
            cycle.add(course)
            course_prerequisits = adj.get(course,None)
            if not course_prerequisits:
                output.append(course) #no prerequisits needed
            else: 
                #are all course in output already? 
                if not set(course_prerequisits) - set(output):
                    output.append(course)                    
                for cpr in course_prerequisits:
                    if cpr not in output:                    
                        if dfs(cpr)==False:
                            return False
                        output.append(course)
                    return True
            return True 

        visited = set()
        cycle = set()
        output = []
        for c in courses:
            if c not in output:
                if dfs(c)==False:
                    return []                
                cycle.remove(c)
                visited = set()
        
        if len(output)<numCourses:
            missing_courses = numCourses - len(output)
            for i in range(len(output),len(output) + missing_courses):
                output.append(i)

        return output
    
if __name__=='__main__':
    print ("START...")

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    numCourses = 13
    prerequisites = [[0,1]]

    s = Solution()
    res = s.findOrder(numCourses, prerequisites)
    print ('res:=',res)

    print ("END")
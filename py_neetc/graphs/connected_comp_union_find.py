
#find number of connected components

class Solution:

    def countComponenets(self, edges):
        
                
        def find(n1): #find root parent
            
            if n1!=child_parent[n1]:
                child_parent[n1] = find(child_parent[n1])
            return child_parent[n1] 

        def union(n1,n2):
            #find root parent of each node
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return 0 #no union to perform
            
            if rank[p2]>rank[p1]: #where to add the children to p1 or p2?
                child_parent[p1] = p2 #new Parent for p2
                rank[p2] += rank[p1]
            else:
                child_parent[p2] = p1   #new Parent for p1
                rank[p1] += rank[p2]
            return 1


        #step 1: build a child_parent dictionary where each child IS the parent (for now)
        #        build rank dictionary so we can tell HOW to associate which set (smaller to bigger and not reversed)
        my_set = set()
        for e in edges:
            my_set.add(e[0])
            my_set.add(e[1])
        
        child_parent = {}#K=child, V=parent
        rank = {}
        for i in my_set:
            child_parent[i]=i
            rank[i] = 1 #assume 1 for now

        #setp 2: assume all links are detached, if we find a union - we decrement a link
        res = len(child_parent)
        for n1, n2 in edges:
            v = union(n1,n2)
            res -= v

        return res



if __name__=='__main__':
    print ("Start...")
 
    edges =  [['A','B'],['I','Z'],['M','N'],['C','B'],['J','Q'],['B','Q'],['V','I']]

    s = Solution()
    counter = s.countComponenets(edges)
    print ('counter:=',counter)

    print ("END")
    
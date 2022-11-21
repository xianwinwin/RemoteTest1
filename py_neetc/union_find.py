from collections import defaultdict

class UnionFind:

    def findRedundantConnection(self, edges):
        self.graph = defaultdict(list)

        def union(px,py):

            if px==py:
                return False

            values_x = self.graph.get(px,None)
            values_y = self.graph.get(py,None) 

            if (not values_x and not values_y) or (values_x and not values_y):
                self.graph[px].append(py)
            elif values_y and not values_x:
                self.graph[py].append(px)
            elif values_x and values_y: 
                del self.graph[py]
                self.graph[px].extend(values_y)
                self.graph[px].append(py)
            
            return True
        
        def find(item):
            #find the parent, if none exists - return the item as a parent
            if self.graph.get(item, None):
                return item

            for k,v in self.graph.items():
                if item in v:
                    return k
            
            return item

        for e in edges:            
            x,y = e[0], e[1]    

            if x==2 and y==5:
                print ("ALT")

            parent_x = find(x) 
            parent_y = find(y)

            f = union(parent_x, parent_y)
            if not f:
                return e


if __name__=='__main__':
    print("start...")

    edges =[[1,2],[2,3],[3,4],[1,4],[1,5]]#[[1,2],[1,3],[2,3]]    
    uf = UnionFind()
    e = uf.findRedundantConnection(edges)
    print ('e:=',e)
    

    print ("END")
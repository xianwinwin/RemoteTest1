from collections import defaultdict

class Solution:

    def accountsMerge(self, accounts):

        def union(e1,e2):
 
            p1 = find(e1)
            p2 = find(e2)
 
            if p1==p2: #same parent (already together)
                return 

            #union them together, how? depends on the ranking (bigger takes it all)
            if ranking[p2]>ranking[p1]:
                child_parent[p1] = p2 #p2 now is the Father
                ranking[p2]+=ranking[p1]
            else:
                child_parent[p2] = p1 #p1 is child and p2 is the father
                ranking[p1]+=ranking[p2]

        def find(e):
            #looking for the father of e  (as dfs);
            if child_parent[e] != e:
                child_parent[e] = find(child_parent[e])            
            return child_parent[e] 

        child_parent  = {} #K=child's email, V=parent's email 
        ranking = {}
        email_name = {} #K=email V=name
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            for email in emails:
                email_name[email]=name
                child_parent[email] = email
                ranking[email]=1


        #union graph such that child point to paraent
        for acct in accounts:
            emails = acct[1:]
            for e1, e2 in zip(emails, emails[1:]):
                union(e1,e2)


        #iterate graph to get the parent results with 
        cached = defaultdict(list) #K=parent with list of childs
        for c in child_parent.keys():
            p = find(c) #why like this? because we need to know who's the parent of the parent when x=parent[x]
            cached[p].append(c)
 
        #retrun desired list [[name,[emails],...]]
        res = []
        for p,childs in cached.items():
            parent_name = email_name[p]
            row = [parent_name] + sorted(childs)
            res.append(row)

        return res


if __name__=='__main__':
    print ("Start")

    s = Solution()

    n = [   ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]
        ] 

    res = s.accountsMerge(n)
    for r in res:
        print (r)

    print ("END")
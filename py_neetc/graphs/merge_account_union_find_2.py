from collections import defaultdict

class Solution:

    def accountsMerge(self, accounts):

        def union(x,y):
            
            if x=='David1@m.co':
                print ("alt")


            r1 = find(x)
            r2 = find(y)

            if r1!=r2:
                parents[r2] = r1
 

        def find(x): 
            if parents[x]!=x:
                parents[x]=find(parents[x])
            
            return parents[x]

        parents = {}
        emailToName = {}

        for acct in accounts:
            name = acct[0]
            for email in acct[1:]:
                emailToName[email]=name
                parents[email]=email
        
        for acct in accounts:
            email1 = acct[1]
            for email2 in acct[2:]:
                union(email1,email2)
            
        groups = defaultdict(list)

        for email in parents:
            r = find(email)
            groups[r].append(email)
 
        ans = []

        for key in groups:
            ans.append([emailToName[key]] + sorted(groups[key]))

        return ans


if __name__=='__main__':
    print ("Start...l")

    s = Solution()

    n = [   ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]
        ]

    n = [
            ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
            ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
            ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
            ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
        ]

    n = [
            ["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]
        ]

    res = s.accountsMerge(n)
    for r in res:
        print (r)

    print ("END")
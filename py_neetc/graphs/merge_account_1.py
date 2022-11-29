from collections import defaultdict

class Solution:

    def accountsMerge(self, accounts):

        graph = defaultdict(set) #holds k=root_email and v=all users emails
        visited = {} # k = root_email; v = NAME
        rooters = {} # k = email v = root email
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            root_email = emails[0]

            #option 1: one of the emails already seen - attache it to the root_email
            flag = False
            for email in emails:
                if visited.get(email,None): 
                    root_email = rooters[email]
                    user_emails = graph.get(root_email, None)
                    if user_emails:
                        flag = True
                        user_emails.update(emails)
                        graph[root_email] = user_emails
                
                rooters[email] = root_email
                visited[email] = name
             
            if flag:
                continue

            graph[root_email].update(emails)


        #return results
        res = []
        for root_email, emails in graph.items():
            name = visited[root_email]
            res.append( [name] + sorted(list(emails)) )

        return res



if __name__=='__main__':
    print ("Start")

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
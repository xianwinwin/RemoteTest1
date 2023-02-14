from collections import deque

num = 7123
base = 10
dq = deque()
while num>0:
    reminder = num%base
    res = reminder//(base//10)
    dq.appendleft(res)
    num = num - reminder
    base = base * 10
    
print (dq)


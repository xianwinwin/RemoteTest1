#https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city to i 
with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst 
with at most k stops. If there is no such route, return -1.

USING Bellman–Ford Algorithm

high leve:
    1. use a dictionary 'PRICES' to set the K=Name V=price/weight; since we dont know, we use:
       K=Name and float('inf') for the src we can use K=Name and V=0

    1. there are 2 for loops: outer for temp_vales (from previous inner iteration)
    2  inner itreation: see if the price at [s] + the price of destination is LESS then temp (which may be inf)
    3. if so update temp_price with the new price tag 

    when you iterate like this you will get to the destination with the minimum price UNLESS you stopped earlier


Time Complexity of Bellman Ford algorithm is relatively high O ( V ⋅ E ) , in case E = V 2 , O ( V 3 ) .
'''

import heapq
from collections import deque, defaultdict

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k):

        #step 1: get all terminal names and creat a dict (prices) with inf except price[src]
        terminals = set()
        for f in flights:
            terminals.add(f[0])
            terminals.add(f[1])

        prices = {}
        for t in terminals:
            prices[t]=float("inf")
        
        prices[src]=0 #no cost to go from src to src

        #outer for loop will give us the number of stop we wish to have (if len(prices) ) you'll get the most minimal
        for i in range (0,k+1):
            temp_prices = prices.copy()

            for s,d,p in flights: #s=start, d=destination, p=price
                if prices[s]==float('inf'): 
                    continue
                if prices[s]+p <temp_prices[d]: # is the price at s can be improved with another way to get there?
                    temp_prices[d]=prices[s]+p #updateing the temp_price (for this round!!! not the prices)
                    
            prices = temp_prices #at the end you update the prices 

        
        if not prices.get(dst,None):
            return -1
        if prices.get(dst)==float('inf'):
            return -1
        return prices[dst]
        
if __name__=='__main__':
    print ("Start...")
  
    src = 'A'
    dst = 'F' 
    k = 1
    n = 13
    flights = [ ['A','B',1],['B','C',3.1],['C','E',0.8],['C','D',2.1],['D','G',1.1],['C','F',2.1],
    ['B','F',4],['B','J',0.6],['Q','J',0.5],['A','Q',0.8],['A','M',2],['M','N',4.2],['B','H',3],
    ['H','Z',0.45],['Z','D',5],['A','H',2],['Z','F',0.8]]

    s = Solution()
    price = s.findCheapestPrice(n,flights,src,dst,k)
    print ('price:=',price)
    print ("END")
    
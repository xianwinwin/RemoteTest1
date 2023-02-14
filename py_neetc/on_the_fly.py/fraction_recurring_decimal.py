'''
https://leetcode.com/problems/fraction-to-recurring-decimal/
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format. If the fractional part is repeating, 
enclose the repeating part in parentheses. If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
''' 

class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if denominator==0:
            return None
        
        if numerator==0:
            return '0'
         
        result = numerator/denominator 
        q = numerator//denominator
        r = numerator%denominator
        
        counter = 0
        res = []
        while True:
            numerator = numerator*10
            res.append((numerator//denominator)%10)

            counter+=1
            if counter==100:
                break
        
        print ("_S_")
        print (res)
        num_str = ''.join(map(str,res))
        return str(result)
 

if __name__=='__main__':
    print ("start...")
     
    numerator = 1
    denominator = 17

    s = Solution()     
    r = s.fractionToDecimal(numerator,denominator)
    print ("result:=",r)

    print ("END!")
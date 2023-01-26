'''
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Input: numerator = 4, denominator = 333
Output: "0.(012)"
''' 

class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator==0:
            return '0'
        res = []
        result_sign = '' if (numerator>0 and denominator>0) or (numerator<0 and denominator<0) else '-' 
        numerator = abs(numerator)
        denominator = abs(denominator)

        q, r = divmod(numerator, denominator)
        
        res.append(result_sign)
        res.append(q)
        res.append('.')
        
        reminders = []
        is_repetition = True
        while r not in reminders:
            reminders.append(r)
            numerator = numerator*10
            q,r = divmod(numerator, denominator)            
            res.append(q%10)
            if r==0:
                is_repetition=False    
        
        if res[-1]==0:
            res = res[0:-1]
        
        #repetition location
        repetition_starts = -1
        for i, lr in enumerate(reminders):
            if lr==r:
                repetition_starts=i
                 
        dot_index = res.index('.')
        prefix = ''.join(map(str,res[0:dot_index+1]))        
        pattern = ''.join(map(str,res[dot_index+1:]))
        if is_repetition:            
            if repetition_starts>0:
                a = pattern[0:repetition_starts]
                b = pattern[repetition_starts:]
                pattern=a+"("+b+")"
            else:
                pattern = '('+pattern+')'
            return prefix+pattern
        if not pattern:
            return prefix[0:-1] #without the dot
        return prefix+pattern


if __name__=='__main__':
    print ("start...")
    
    numerator = -22
    denominator = -11
    print ("result-->",numerator/denominator)
    s = Solution()     
    r = s.fractionToDecimal(numerator, denominator)
    print (" Fraction to Recurring Decimal:=",r)

    print ("END!")
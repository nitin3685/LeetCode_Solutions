class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x < (-2**31) or x > ((2**31)-1):
            return 0
        
        rem_x = abs(x)
        rev_x = 0
        while rem_x != 0:
            rev_x =  (rev_x * 10 ) + (rem_x % 10) 
            rem_x = rem_x // 10
        if rev_x < (-2**31) or rev_x > ((2**31)-1):
            return 0
        elif x < 0:
            return (-1 * rev_x)
        else:
            return rev_x

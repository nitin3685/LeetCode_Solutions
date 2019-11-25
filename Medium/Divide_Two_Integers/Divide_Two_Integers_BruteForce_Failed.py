class Solution:
'''
Will Fail for print (Solution().divide(-2147483648, -1))
It is too slow
'''
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        result = 0
        if (dividend > 0 and divisor > 0):
            while divisor <= dividend:
                dividend -= divisor
                result += 1
        elif (dividend < 0 and divisor < 0):
            while dividend <= 0:
                dividend -= divisor
                result += 1
            result -= 1
        elif (divisor < 0):
            while dividend >= 0:
                dividend += divisor
                result -= 1
            result += 1
        else:
            while dividend <= 0:
                dividend += divisor
                result -= 1
            result += 1
            
        return result

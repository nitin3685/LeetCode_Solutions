class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        res = 0
        num = min(A)
        while num :
            res += num%10
            num = int(num/10)
        return  1 if (res % 2 == 0) else 0
        

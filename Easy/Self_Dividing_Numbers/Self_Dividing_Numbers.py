class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        def self_dividing(num):
            for char in str(num):
                if char == '0' or (num%int(char)) != 0:
                    return False
            return True
        for num in range (left,right+1):
            if self_dividing(num):
                res.append(num)
        return res
        

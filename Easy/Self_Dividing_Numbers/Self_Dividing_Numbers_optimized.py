class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range (left,right+1):
            flag = 1
            for char in str(num):
                if char == '0' or (num%int(char)) != 0:
                    flag = 0
                    break
            if flag:
                res.append(num)
        return res
        

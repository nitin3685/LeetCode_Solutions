class Solution:
    def isArmstrong(self, N: int) -> bool:
        num_str=str(N)
        len_num = len(num_str)
        res = 0
        for char in num_str:
            res += int(char)**len_num
        return (res == N)
        

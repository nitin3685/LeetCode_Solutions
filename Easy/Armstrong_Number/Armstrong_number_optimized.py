class Solution:
    def isArmstrong(self, N: int) -> bool:
        num_str=str(N)
        len_num = len(num_str)

        return (N == sum([int(char)**len_num for char in num_str]))
        

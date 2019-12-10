class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict_A = {}
        for index,num in enumerate(A):
            if num not in dict_A.keys():
                dict_A[num] = index
            else:
                return num
        
        

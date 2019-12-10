class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict_A = {}
        #Use set to make it faster
        for index,num in enumerate(A):
            if num not in dict_A.keys():
                dict_A[num] = index
            else:
                return num
        
        

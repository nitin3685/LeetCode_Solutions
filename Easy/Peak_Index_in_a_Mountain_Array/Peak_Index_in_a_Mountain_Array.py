
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = 0
        peak_num = A[0]
        for index,num in enumerate(A[1:]):
            if num > peak_num:
                peak = index+1
                peak_num = num
            else:
                return peak
        
        

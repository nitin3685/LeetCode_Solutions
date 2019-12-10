class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        right = len(A) - 1
        left = 0
        while left<right:
            mid = left + (right - left) // 2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
        

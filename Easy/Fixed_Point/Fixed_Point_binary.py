class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        left = 0
        right = len(A) - 1
        while left<right:
            mid = left + (right-left)//2
            if A[mid] > mid:
                right = mid-1
            elif A[mid] < mid:
                left = mid+1
            else:
                right = mid
        return left if A[left] == left else -1

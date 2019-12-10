class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for index,num in enumerate(A):
            if num == index:
                return index
        return -1

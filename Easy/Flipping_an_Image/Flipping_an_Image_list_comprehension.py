class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[int(not i) for i in row[::-1]] for row in A]

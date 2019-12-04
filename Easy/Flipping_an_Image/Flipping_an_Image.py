class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        FI_A = list()
        for row in A:
            row = [0 if i else 1 for i in row[::-1]]
            FI_A.append(row)
        return FI_A

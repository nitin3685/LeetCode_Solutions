#Weird algorithm for matrix multiplication. just addition will produce result matrix
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        col = [0] * m
        ans = 0
        for r,c in indices:
            row[r] += 1
            col[c] += 1
        for i in range(n):
            for j in range(m):
                ans += (row[i] + col[j] )%2
        
        return ans

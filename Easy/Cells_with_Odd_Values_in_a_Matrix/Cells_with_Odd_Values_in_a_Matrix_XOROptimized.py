class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row=[False]*n
        col=[False]*m
        odd_rows=0
        odd_cols=0
        
        for (r,c) in indices:
            row[r] ^= True
            odd_rows += 1 if row[r] else -1            
            col[c] ^= True
            odd_cols += 1 if col[c] else -1            
        return (odd_rows*(m-odd_cols) + (n-odd_rows)*odd_cols)

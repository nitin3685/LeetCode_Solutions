class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for col_str in zip(*A):
            if list(col_str) != sorted(col_str):
                res += 1
        return res

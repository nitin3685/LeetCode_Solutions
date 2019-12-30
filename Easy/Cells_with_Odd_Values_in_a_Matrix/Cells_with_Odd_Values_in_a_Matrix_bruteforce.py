class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        import numpy as np
        res = np.zeros((n,m))
        for index in  indices:
            res[index[0]] += 1
            res[:,index[1]] += 1
        return np.count_nonzero(res%2)

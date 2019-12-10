class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        c = Counter(arr)
        return len(set(c.values())) == len(c)

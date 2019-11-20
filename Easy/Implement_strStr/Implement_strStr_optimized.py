class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        
        return haystack.find(needle)

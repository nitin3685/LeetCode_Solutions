class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_needle = len(needle)
        for index,char in enumerate(haystack):
            if haystack[index:index+len_needle] == needle:
                return index
        return -1
        

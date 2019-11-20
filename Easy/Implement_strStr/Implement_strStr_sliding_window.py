class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_needle = len(needle)
        len_haystack = len(haystack)
        length = len_haystack - len_needle + 1
        for i in range(length):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lcp = ""
        shortest = min(strs, key=len )
        len_shortest = len(shortest)
        for i in range (len_shortest):
            if all(string.startswith(shortest[:len_shortest-i]) for string in strs):
                lcp = shortest[:len_shortest-i]
                break
        return lcp

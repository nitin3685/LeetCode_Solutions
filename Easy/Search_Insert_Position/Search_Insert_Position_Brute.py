class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        sub = ''
        for ind,char in enumerate(s):
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                sub = sub[sub.index(char)+1:] + char
        return ans
            

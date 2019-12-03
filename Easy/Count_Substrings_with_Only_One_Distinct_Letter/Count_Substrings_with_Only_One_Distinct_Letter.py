class Solution:
    def countLetters(self, S: str) -> int:
        if len(S) == 1:
            return 1
        prev_char = S[0]
        res = 1
        flag = 1
        for cur_char in S[1:]:
            if cur_char == prev_char:
                flag += 1
                res += flag
            else:
                prev_char = cur_char
                flag = 1
                res += 1
        return res

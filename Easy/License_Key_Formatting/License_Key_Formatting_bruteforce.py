class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        lkey = "".join(S.split("-")).upper()
        len_lkey = len(lkey)-1
        res = ""
        for index,char in enumerate(lkey[::-1]):
            res+=char
            if (index+1)%K == 0 and index != len_lkey:
                res+='-'     
        return res[::-1]
        

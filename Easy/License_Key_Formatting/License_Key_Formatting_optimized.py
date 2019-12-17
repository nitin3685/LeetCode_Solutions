class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        lkey = S.replace("-","").upper()
        len_lkey = len(lkey)
        
        first_block = lkey[:(len_lkey%K)] 
        blocks = [lkey[i:i+K] for i in range (len_lkey%K,len_lkey,K)]
           
        if first_block and blocks : return first_block+"-"+"-".join(blocks) 
        elif first_block : return first_block
        else: return "-".join(blocks)

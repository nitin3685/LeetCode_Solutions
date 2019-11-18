class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        sub_s_len = 0
        
        for i in range(s_len):
            uniq_letter_list = [s[i]]
            for j in range(i+1,s_len):
                if s[j] not in uniq_letter_list:
                    uniq_letter_list.append(s[j])
                else:
                    break
            if len(uniq_letter_list) > sub_s_len:
                sub_s_len = len(uniq_letter_list)
        return sub_s_len
            

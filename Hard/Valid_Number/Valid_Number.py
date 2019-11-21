#Will reject decimal exponent which is mathematically wrong but LeetCode tests for it
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        
        signs = ['+', '-']
        
        def isValidNum(num: str) -> bool:
            if not num:
                return False
            num_list = ['0','1','2','3','4','5','6','7','8','9']
            for char in num:
                if char not in num_list: return False
            return True
        
        def isValidDecimalNum(dec_num:str)-> bool:
            if '.' not in dec_num:
                return isValidNum(dec_num)
            if dec_num == '.':
                return False
            else:
                if number[0] == '.':
                    return isValidNum(dec_num[1:])
                elif number[-1:] == '.':
                    return isValidNum(dec_num[:-1])
                
                whole_number,fraction_number= dec_num.split('.',1)
                print(whole_number,fraction_number)
                return (isValidNum(whole_number) and isValidNum(fraction_number))

        
        #Get number and exponent
        if s[-1:] == 'e' or s[0] == 'e': return False

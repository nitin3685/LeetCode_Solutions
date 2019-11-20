class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1, 
                      'V' : 5,
                      'X' : 10,
                      'L' : 50,
                      'C' : 100,
                      'D' : 500,
                      'M' : 1000,
                      'IV': 4,
                      'IX': 9,
                      'XL': 40,
                      'XC': 90,
                      'CD': 400,
                      'CM': 900                
                     }
        
        result = 0
        skip = 0
        for index,char in enumerate(s):
            if skip:
                skip = 0
                continue
            if index == (len(s)-1):
                if not skip:
                    result += roman_dict[char]
                break
            if s[index:index+2] in roman_dict:
                result += roman_dict[s[index:index+2]]
                skip = 1
            else:
                result += roman_dict[char]
                skip = 0
        return result

        

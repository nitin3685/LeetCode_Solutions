class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1, 
                      'V' : 5,
                      'X' : 10,
                      'L' : 50,
                      'C' : 100,
                      'D' : 500,
                      'M' : 1000              
                     }
        
        result = 0
        prev = 0 
        for char in s[::-1]:
            curr = roman_dict[char]
            if curr < prev :
                result -= curr
            else:
                result += curr
            prev = curr

        return result

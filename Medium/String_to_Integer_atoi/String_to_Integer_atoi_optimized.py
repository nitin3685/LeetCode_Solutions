class Solution:
    def myAtoi(self, str: str) -> int:
        s = str
        if not s:
            return 0
        s = s.strip()
        if s == "":
            return 0
        multiplier = 1
        if s[0] == '+':
            multiplier = 1
            s = s[1:]
        elif s[0] == '-':
            multiplier =  -1
            s = s[1:]
        elif not s[0].isdigit():
            return 0
        result = ""
        for char in s:
            if char.isdigit():
                result = result+char
            else:
                break
        if result != "":
            return min(max(multiplier * int(result),-2**31),2**31-1)
        else:
            return 0
        
                
                
        
        

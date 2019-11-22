class Solution:
    def myAtoi(self, str: str) -> int:
        s = str
        if not s:
            return 0
        s = s.strip()
        print(s)
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
        print (s)
        for char in s:
            if char.isdigit():
                result = result+char
            else:
                break
        if result != "":
            int_max = (2**31) - 1
            int_min = -(2**31)
            number = int(result) * multiplier
            if number > int_max: return int_max
            elif number < int_min : return int_min
            else: return number
        else:
            return 0
        
                

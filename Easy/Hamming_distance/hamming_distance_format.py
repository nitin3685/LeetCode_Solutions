#https://docs.python.org/3.4/library/string.html
#Refer to Format Specification Mini-Language section to understand

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)
        b = bin(y)
        
        a = "{:0>33}".format(a[2:])
        b = "{:0>33}".format(b[2:])
        
        ham = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                ham += 1
        
        return ham

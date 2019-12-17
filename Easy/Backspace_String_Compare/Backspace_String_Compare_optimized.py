class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        fS = []
        for index,char in enumerate(S):
            if char == '#':
                if fS:fS.pop()
            else:
                fS.append(char)
        fT = []
        for index,char in enumerate(T):
            if char == '#' :
                if fT:fT.pop()
            else:
                fT.append(char)    
        return fS == fT

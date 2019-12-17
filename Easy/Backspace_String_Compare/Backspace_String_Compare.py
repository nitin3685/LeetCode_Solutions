class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack = []
        for index,char in enumerate(S):
            if char == '#':
                if len(stack):stack.pop()
            else:
                stack.append(char)
        fS = str(stack)
        stack = []
        for index,char in enumerate(T):
            if char == '#' :
                if len(stack):stack.pop()
            else:
                stack.append(char)
        fT = str(stack)
        
        return fS == fT

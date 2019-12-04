class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        balance = 0
        for index,paranthesis in enumerate(S):
            
            if balance == 0 and paranthesis == '(':
                start_index = index 
                balance += 1
            elif paranthesis == '(':
                balance += 1
            else:
                balance -= 1                
            if balance == 0:
                res += S[start_index+1:index]
                
        return res
                

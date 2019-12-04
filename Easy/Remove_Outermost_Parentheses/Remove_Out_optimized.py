class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        counter = 0
        output = ""
        for i in S:
            if i == '(':
                if counter != 0:
                    output += '('
                counter += 1
                    
            else:
                if counter != 1:
                    output += ')'
                counter -= 1
        
        return output

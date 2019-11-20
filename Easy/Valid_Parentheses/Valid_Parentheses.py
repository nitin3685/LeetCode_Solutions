class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        bracket_list = list()
        open_bracket_dict = {'(':')',
                             '[':']',
                             '{':'}'}
        for char in s:
            if char in open_bracket_dict:
                bracket_list.append(char)
            elif not bracket_list:
                return False
            else:
                last_bracket = bracket_list.pop()
                if open_bracket_dict[last_bracket] == char:
                    continue
                else:
                    return False
        if bracket_list:
            return False
        return True

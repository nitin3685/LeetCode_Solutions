class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in str])
    


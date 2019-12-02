class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(['[.]' if char == '.' else char for char in address])

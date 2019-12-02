class Solution:
    def removeVowels(self, S: str) -> str:
        if not S:
            return S
        return "".join([char for char in S if char not in ['a','e','i','o','u'] ])

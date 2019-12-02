class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        return [B.index(num) for num in A ]
        

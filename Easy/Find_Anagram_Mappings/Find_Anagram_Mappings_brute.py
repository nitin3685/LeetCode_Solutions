class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        B_dict = {num:index for index,num in enumerate(B)}
        return [B_dict[num] for num in A]
        

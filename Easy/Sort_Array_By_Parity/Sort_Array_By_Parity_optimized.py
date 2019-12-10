class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        even = [n for n in A if n%2==0]
        odd = [n for n in A if n%2 != 0]
        return even + odd

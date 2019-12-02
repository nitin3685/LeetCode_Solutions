class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not S or not J:
            return 0
        x = 0
        return len ([stone for stone in S if stone in  J])
        

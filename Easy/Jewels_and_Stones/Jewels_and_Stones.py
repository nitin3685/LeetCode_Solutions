class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not S or not J:
            return 0
        jewels = 0
        for stone in S:
            if stone in J:
                jewels=jewels+1
        return jewels

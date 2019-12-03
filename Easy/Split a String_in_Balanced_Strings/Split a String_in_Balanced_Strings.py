class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for char in s:
            if char == 'L':
                balance += 1
            elif char == 'R':
                balance -= 1
            if balance == 0:
                count += 1
        return count
        
        

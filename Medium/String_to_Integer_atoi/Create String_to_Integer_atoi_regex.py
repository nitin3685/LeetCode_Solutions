class Solution:
    def myAtoi(self, str: str) -> int:
        result = re.search( '^[+-]?\d+', str.strip())
        result = int(result[0] if result else 0)
        return min(max(result,-2**31),2**31-1)

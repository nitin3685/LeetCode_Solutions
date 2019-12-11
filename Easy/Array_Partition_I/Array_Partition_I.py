class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i,res = 0,0
        while i < len(nums):
            res += sorted_nums[i]
            i += 2
        return res
        

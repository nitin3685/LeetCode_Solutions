class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        #faster    
        #nums.sort()
        #return sum(nums[::2])
        

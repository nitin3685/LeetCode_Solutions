class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        dict_nums = dict()
        for ind,num in enumerate(nums):
            if target - num in dict_nums:
                return ind,dict_nums[target - num]
            dict_nums[num] = ind
        return [None,None]

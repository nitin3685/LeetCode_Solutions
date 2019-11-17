class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        dict_nums = {nums[i]:i for i in range(len_nums)}

        for ind,num in enumerate(nums):
            if target - num in dict_nums and dict_nums[target - num] != ind:
                return ind,dict_nums[target - num]
        return [None,None]

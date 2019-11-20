class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        prev_index = 0
        for num in nums[1:]:
            if num == prev:
                continue
            else:
                prev = num
                prev_index += 1
                nums[prev_index] = num
        return prev_index+1
        

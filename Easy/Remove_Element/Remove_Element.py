class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr_index = 0
        for index,num in enumerate(nums):
            if num != val:
                nums[curr_index] = num
                curr_index += 1
        return curr_index
                

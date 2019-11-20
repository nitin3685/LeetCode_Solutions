class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] == val:
                nums[i] = nums[len_nums - 1]
                len_nums -= 1
            else:
                i += 1
        return len_nums
            
                

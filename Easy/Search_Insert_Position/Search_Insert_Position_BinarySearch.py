class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_num = len(nums)
        
        if len_num == 0 or target <= nums[0] :
            return 0
        if target > nums[len_num-1]:
            return len_num
        
        left_index = 0
        right_index = len_num - 1
        middle_index = 0
        
        while left_index < right_index:
            middle_index = (left_index + right_index)//2
            
            if (target > nums[middle_index]):
                left_index = middle_index + 1
            elif(target < nums[middle_index]):
                right_index = middle_index
            else:
                return middle_index
        if target < nums[middle_index]:return middle_index
        return middle_index+1
            
                
            

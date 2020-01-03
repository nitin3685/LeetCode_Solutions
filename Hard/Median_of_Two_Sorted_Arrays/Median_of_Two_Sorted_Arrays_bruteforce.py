#Complexity is not O(log(m+n))
#Solution expects the above specified complexity
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1[:]
        res.extend(nums2)
        res = sorted(res)
        len_res = len(res)
        if len_res % 2 == 0 :
            return (res[len_res//2] + res[(len_res//2)-1] )/2
        else:
            return (res[(len_res//2)])

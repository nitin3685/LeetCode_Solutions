class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        if(len_nums1 > len_nums2):
            return (self.findMedianSortedArrays(nums2,nums1))
        

        low = 0
        high = len_nums1
        while(low <= high):
        
            partitionnums1 = (low + high)//2 
            partitionnums2 = ((len_nums1 + len_nums2 + 1) //2 ) - partitionnums1
            
            maxLeftnums1 = float("-inf") if  partitionnums1 == 0 else nums1[partitionnums1-1]
            minRightnums1 = float("inf")  if  partitionnums1 == len_nums1 else nums1[partitionnums1]

            maxLeftnums2 = float("-inf") if  partitionnums2 == 0 else nums2[partitionnums2-1]
            minRightnums2 = float("inf")  if  partitionnums2 == len_nums2 else nums2[partitionnums2]
            print(maxLeftnums1,minRightnums1,maxLeftnums2,minRightnums2)
            if (maxLeftnums1 <= minRightnums2 and maxLeftnums2 <= minRightnums1):
                if ((len_nums1+len_nums2)%2 == 0):
                    print(max(maxLeftnums1,maxLeftnums2),min(minRightnums1,minRightnums2))
                    return (max(maxLeftnums1,maxLeftnums2) + min(minRightnums1,minRightnums2))/2
                else:
                    return max(maxLeftnums1,maxLeftnums2) 
            elif (maxLeftnums1 > minRightnums2):
                    high = partitionnums1 - 1
            else:
                    low = partitionnums1 + 1
                    
        return 0
        
#https://www.youtube.com/watch?v=LPFhl65R7ww
        
            

                

        

        
        

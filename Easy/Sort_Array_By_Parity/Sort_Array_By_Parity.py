class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        rev_index = len(A) - 1
        if not rev_index:
            return A
        B = A[:]
        for index,num in enumerate(A):
            if num%2 == 0:
                continue
            while rev_index > 0 and B[rev_index]%2 != 0:
                rev_index -= 1
            if rev_index > index:
                B[index] = B[rev_index]
                B[rev_index] = num
            else:
                break
        return B

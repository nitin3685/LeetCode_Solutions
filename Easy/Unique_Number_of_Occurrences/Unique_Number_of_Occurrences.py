class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_set = set(arr)
        count_set = set()
        for num in num_set:
            if arr.count(num) in count_set:
                return False
            count_set.add(arr.count(num))
        return True
            

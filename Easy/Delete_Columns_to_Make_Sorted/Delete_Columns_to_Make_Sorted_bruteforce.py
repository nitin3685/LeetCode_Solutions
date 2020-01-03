class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        from collections import defaultdict
        columns = defaultdict(list)
        for string in A:
            for index,char in enumerate(string):
                columns[index].append(ord(char))
        res = 0
        for index,column in columns.items():
            if not all(column[i]<=column[i+1] for i in range(len(column)-1)):
                res += 1
        return res
            

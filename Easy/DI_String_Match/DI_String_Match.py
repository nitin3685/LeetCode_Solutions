class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lowest = 0
        highest = len(S)
        res = list()
        for char in S:
            if char == 'I':
                res.append(lowest)
                lowest += 1
            else:
                res.append(highest)
                highest -= 1
        if char == 'I':
            res.append(lowest)
        else:
            res.append(highest)

        return res
                

class MovingAverage:
    import collections
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = collections.deque()
        self.sum = 0
        self.len = 0

    def next(self, val: int) -> float:
        if self.len == self.size:
            self.sum -= self.nums.popleft()
            self.sum += val
            self.nums.append(val)
        else:
            self.sum += val
            self.nums.append(val)
            self.len += 1
            
        return self.sum/self.len
        

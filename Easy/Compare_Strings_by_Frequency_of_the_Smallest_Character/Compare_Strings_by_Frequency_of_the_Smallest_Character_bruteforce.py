class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        word_freq = [word.count(min(word)) for word in words]
        res = []
        for query in queries:
            query_freq = query.count(min(query))
            res.append(sum(query_freq < f for f in word_freq))
        return res

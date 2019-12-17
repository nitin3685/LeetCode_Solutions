class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        from bisect import bisect
        word_freq = sorted(word.count(min(word)) for word in words)
        len_words = len(words)
        return [len_words - bisect(word_freq,q.count(min(q))) for q in queries]
            
            
            

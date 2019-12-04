class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            morse = "".join([morse_list[ord(letter)-ord('a')] for letter in word])
            res.add(morse)
        return len(res)

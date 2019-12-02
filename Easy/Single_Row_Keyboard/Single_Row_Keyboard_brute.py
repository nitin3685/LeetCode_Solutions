class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict_keyboard = { key:index for index,key in enumerate(keyboard)}
        pos = 0
        time = 0
        for char in word:
            time += abs(pos-dict_keyboard[char])
            pos = dict_keyboard[char]
        return time        

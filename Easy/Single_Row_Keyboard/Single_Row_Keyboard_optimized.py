class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict_keyboard = { key:index for index,key in enumerate(keyboard)}
        prev_pos = 0
        time = 0
        for char in word:
            cur_pos = dict_keyboard[char]
            time += abs(cur_pos-prev_pos)
            prev_pos = cur_pos
        return time        

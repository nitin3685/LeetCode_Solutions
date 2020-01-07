class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        import queue
        word_queue = queue.Queue()
        res = list()
        len_of_words = 0
        for word in words:
            if (len_of_words + word_queue.qsize() + len(word)) <= maxWidth:
                word_queue.put(word)
                len_of_words += len(word)
            else:
                sentence = ""
                if word_queue.qsize() == 1:                  
                    #only one word in this sentence.
                    #append the remaining spaces
                    sentence += word_queue.get()
                    num_space_to_pad = (maxWidth - len_of_words)
                    sentence += " " * num_space_to_pad
                else:  
                    #no more words can be fit into current sentence
                    #construct the sentence 
                    #calculate minimum number of spaces per word 
                    #and remaining spaces to adjust
                    min_num_space_per_word = (maxWidth - len_of_words) // (word_queue.qsize() - 1)
                    remaining_space = (maxWidth - len_of_words) % (word_queue.qsize() - 1)
                    while word_queue.qsize() > 1:
                        sentence += word_queue.get()
                        sentence += " " * min_num_space_per_word
                        if remaining_space:
                            sentence += " "
                            remaining_space -= 1
                    sentence += word_queue.get()
                res.append(sentence)
                len_of_words = len(word)
                word_queue.put(word)

        sentence = ""
        if word_queue.qsize() == 1:                  
            #only one word in this sentence.
            #append the remaining spaces
            sentence += word_queue.get()
            num_space_to_pad = (maxWidth - len_of_words)
            sentence += " " * num_space_to_pad
        else:  
            #For the last line of text, it should be left justified 
            #and no extra space is inserted between words
            spaces_added = 0
            while word_queue.qsize() > 1:
                sentence += word_queue.get()
                sentence += " "
                spaces_added += 1
            sentence += word_queue.get()
            num_space_to_pad = (maxWidth - len_of_words - spaces_added)
            sentence += " " * num_space_to_pad 
        res.append(sentence)
        
        return res

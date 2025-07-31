class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}
        s_list = s.split(' ')
        if len(s_list) != len(pattern) :
            return False
        for char,word in zip(s_list,pattern) :
            if char in char_to_word :
                if char_to_word[char] != word :
                    return False
            elif word in word_to_char :
                if word_to_char[word] != char :
                    return False    
            else :
                char_to_word[char] = word
                word_to_char[word] = char
        return True
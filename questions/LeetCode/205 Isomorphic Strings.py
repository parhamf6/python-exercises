class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            #check if the mapping are consistent 
            if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
                return False
            if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
                return False

            #add to the mapping
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True
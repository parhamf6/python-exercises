class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_hash = {}

        for c in magazine:
            maga_hash[c] = 1 + maga_hash.get(c, 0)

        for c in ransomNote:
            if c not in maga_hash or maga_hash[c] <= 0:
                return False
            maga_hash[c] -= 1
        
        return True
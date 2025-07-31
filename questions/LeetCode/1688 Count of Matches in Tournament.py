class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches  = 0
        teams = n
        while teams > 1:
            if teams % 2 == 0:
                matches += teams // 2
                teams = teams // 2
            else:
                matches  += (teams - 1) // 2
                teams = (teams // 2) + 1
        return matches
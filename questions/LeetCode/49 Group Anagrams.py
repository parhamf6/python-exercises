# Version 1: First working solution
# Group words by their sorted characters.
# Works correctly, but the code is a bit verbose and sorting each word costs O(k log k).
# Time: O(n * k log k)
# Space: O(n * k)class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for i in strs:
            temp = []
            for j in i:
                temp.append(j)
            temp.sort()
            temp2 = "".join(temp)
            if temp2 in grp:
                grp[temp2].append(i)
            else:
                grp[temp2]=[i]
        values = list(grp.values())
        return values

# Version 2: Cleaner implementation
# Same algorithm as Version 1, but uses:
# - list(word) instead of manually building a list
# - defaultdict(list) to automatically create an empty list for new keys
# defaultdict(list): creates an empty list automatically when a missing key is accessed.
# Time: O(n * k log k)
# Space: O(n * k)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            temp = list(word)
            temp.sort()
            key = "".join(temp)
            grp[key].append(word)
        return list(grp.values())


# Version 3: Optimized algorithm
# Instead of sorting each word, count the frequency of each letter.
# The 26-letter frequency tuple becomes the dictionary key.
# Counting is O(k), so we avoid the O(k log k) sorting step.
# Time: O(n * k)
# Space: O(n * k)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([b for a,b in sorted([(i,s) for i,s in zip(indices,s)])])

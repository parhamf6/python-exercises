class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(idx, curr_sum, elem):
            if curr_sum == target:
                ans.append(elem[:])
                return
            
            if idx == n or curr_sum > target:
                return
            
            elem.append(candidates[idx])
            backtrack(idx + 1, curr_sum + candidates[idx], elem)
            elem.pop()
            # skipping the duplicates
            while idx + 1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx + 1, curr_sum, elem)
        backtrack(0, 0, [])
        return ans
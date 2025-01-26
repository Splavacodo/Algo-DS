class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        combinations = []
        curr_combo = []
        
        def find_combos(idx, curr_total):
            if curr_total == target:
                combinations.append(curr_combo.copy())
                return
            elif idx == len(candidates) or curr_total > target:
                return 
            
            candidate = candidates[idx]

            curr_combo.append(candidate)
            find_combos(idx + 1, curr_total + candidate)

            curr_combo.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            find_combos(idx + 1, curr_total)
        
        find_combos(0, 0)
        return combinations
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combinations = []
        curr_combo = []

        def find_combos(i, curr_total):
            if i >= len(candidates) or curr_total > target: 
                return
            elif curr_total == target:
                combinations.append(curr_combo.copy())
                return 
            
            curr_combo.append(candidates[i])
            find_combos(i, curr_total + candidates[i])
            
            curr_combo.pop()
            find_combos(i + 1, curr_total)

        find_combos(0, 0)
        return combinations
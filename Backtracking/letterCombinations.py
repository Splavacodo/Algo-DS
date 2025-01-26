class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
        }

        combos = []

        def find_combos(curr_combo, idx):
            if idx == len(digits):
                combos.append(curr_combo)
                return
            
            digit = digits[idx]
            letters = digit_to_letters[digit]

            for letter in letters:
                find_combos(curr_combo + letter, idx + 1)
            
        find_combos("", 0)
        return combos
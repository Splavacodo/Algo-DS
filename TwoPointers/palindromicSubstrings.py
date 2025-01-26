class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                num_palindromes += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                num_palindromes += 1
                left -= 1
                right += 1
        
        return num_palindromes
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = 0
        res_len = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_idx = left
                    res_len = right - left + 1
                
                left -= 1
                right += 1
            
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_idx = left
                    res_len = right - left + 1
                
                left -= 1
                right += 1
        
        return s[res_idx:res_idx + res_len]
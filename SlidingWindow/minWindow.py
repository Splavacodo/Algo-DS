class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matched_chars = {}

        t_char_count = {}

        for char in t:
            t_char_count[char] = t_char_count.get(char, 0) + 1
     
        matches = 0
        left_ptr = 0
        total_t_chars = len(t_char_count)
        min_win_len = float('inf')
        min_win_sub = ""

        for right_ptr in range(len(s)):
            right_char = s[right_ptr]

            if right_char in t_char_count:
                matched_chars[right_char] = matched_chars.get(right_char, 0) + 1

                if t_char_count[right_char] == matched_chars[right_char]:
                    matches += 1
            
            while matches == total_t_chars:
                win_len = (right_ptr - left_ptr) + 1

                if min_win_len > win_len:
                    min_win_len = win_len
                    min_win_sub = s[left_ptr:right_ptr + 1]
                
                left_char = s[left_ptr]
                if left_char in matched_chars:
                    matched_chars[left_char] -= 1

                    if matched_chars[left_char] < t_char_count[left_char]:
                        matches -= 1
                
                left_ptr += 1
        
        return min_win_sub
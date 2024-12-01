def check_inclusion(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    
    In other words, return true if one of s1's permutations is the substring of s2.

    A permutation in this context is an arbitrary rearrangement of all characters in a string. 
    """
    char_counts = {}

    for char in s1: 
        char_counts[char] = char_counts.get(char, 0) + 1
    
    left_ptr = 0
    match_count = 0

    for right_ptr in range(len(s2)):
        s2_char = s2[right_ptr]

        if s2_char in char_counts:
            char_counts[s2_char] -= 1
            if char_counts[s2_char] == 0:
                match_count += 1

        if (right_ptr - left_ptr) + 1 > len(s1):
            left_char = s2[left_ptr]

            if left_char in char_counts and char_counts[left_char] == 0:
                char_counts[left_char] += 1
                match_count -= 1
            elif left_char in char_counts:
                char_counts[left_char] += 1
            
            left_ptr += 1

        if match_count == len(char_counts):
            return True
    
    return False
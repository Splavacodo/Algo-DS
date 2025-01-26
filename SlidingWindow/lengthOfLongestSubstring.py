def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Given a string s, find the length of the longest substring without repeating characters.
        '''
        # Create a set that will hold the characters of the substring
        charSet = set()

        # Create two pointers that will keep track of the longest substring
        left = 0 # right ptr will be taken care of by loop
        longest = 0

        for right in range(len(s)): 
            while s[right] in charSet: 
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            longest = max(longest, (right - left + 1))
        
        return longest
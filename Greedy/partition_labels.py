class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        letter_to_last_idx = {letter : idx for idx, letter in enumerate(s)}
        
        end = -1
        part_sizes = []
        curr_size = 0

        for i in range(len(s)):
            curr_size += 1
            end = max(end, letter_to_last_idx[s[i]])

            if i == end:
                part_sizes.append(curr_size)
                curr_size = 0
            
        return part_sizes

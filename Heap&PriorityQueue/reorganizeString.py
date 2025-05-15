import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_frequencies: dict = {}

        for letter in s:
            char_frequencies[letter] = char_frequencies.get(letter, 0) + 1
        
        max_heap = [(-freq, char) for char, freq in char_frequencies.items()]
        heapq.heapify(max_heap)

        reorganized_chars: list[str] = []

        while len(max_heap) >= 2:
            first_freq, first_char = heapq.heappop(max_heap)
            second_freq, second_char = heapq.heappop(max_heap)

            reorganized_chars.extend([first_char, second_char])

            if first_freq + 1 < 0:
                heapq.heappush(max_heap, (first_freq + 1, first_char))

            if second_freq + 1 < 0:
                heapq.heappush(max_heap, (second_freq + 1, second_char))
        
        if max_heap:
            freq, char = heapq.heappop(max_heap)

            if -freq > 1:
                return ""
            
            reorganized_chars.append(char)
        
        return "".join(reorganized_chars)
from collections import deque

class Solution:
    def foreignDictionary(self, words):
        """Leetcode Prob. 269

        There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

        You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

        Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.
        """
        adj = {letter: set() for word in words for letter in word}
        indegrees = {letter: 0 for letter in adj}

        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i + 1]
            min_len = min(len(first_word), len(second_word))

            if len(first_word) > len(second_word) and first_word[:min_len] == second_word[:min_len]:
                return ""

            for j in range(min_len):
                if first_word[j] != second_word[j]:
                    if second_word[j] not in adj[first_word[j]]:
                        adj[first_word[j]].add(second_word[j])
                        indegrees[second_word[j]] += 1
                
                    break
                    
            queue = deque([letter for letter in indegrees if indegrees[letter] == 0])
            letter_order = []

            while queue:
                curr_letter = queue.popleft()
                letter_order.append(curr_letter)

                for next_letter in adj[curr_letter]:
                    indegrees[next_letter] -= 1

                    if indegrees[next_letter] == 0:
                        queue.append(next_letter)
            
            return "" if len(letter_order) != len(indegrees) else "".join(letter_order)
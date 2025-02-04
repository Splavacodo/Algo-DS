from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_adj[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        sequence_len = 1

        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return sequence_len
                
                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + "*" + curr_word[i + 1:]

                    for neighbor_word in pattern_adj[pattern]:
                        if neighbor_word not in visited:
                            visited.add(neighbor_word)
                            queue.append(neighbor_word)
            
            sequence_len += 1

        return 0

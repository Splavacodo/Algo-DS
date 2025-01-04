class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.prev_words = set()
        self.max_word_length = 0

    def addWord(self, word: str) -> None:
        self.max_word_length = max(self.max_word_length, len(word))
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            
            curr = curr.children[letter]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_word_length:
            return False
        
        if word in self.prev_words:
            return True

        def dfs(node, i):   
            curr = node

            for j in range(i, len(word)):
                letter = word[j]

                if letter == ".":
                    # run dfs to find if there's a possible word 
                    for child_node in curr.children.values():
                        if dfs(child_node, j + 1):
                            self.prev_words.add(word)
                            return True
                    
                    return False
                elif letter not in curr.children:
                    return False
                else:
                    curr = curr.children[letter]
            
            return curr.end_of_word
        
        return dfs(self.root, 0)
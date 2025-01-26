class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            
            curr = curr.children[letter]
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False 
            
            curr = curr.children[letter]
        
        return True
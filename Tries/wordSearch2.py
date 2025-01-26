from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
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

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        rows, cols = len(board), len(board[0])
        curr_word = ""
        matched_words = []

        def find_words(loc, node, word):
            x_loc = loc[0]
            y_loc = loc[1]

            if node.end_of_word:
                matched_words.append(word)
                node.end_of_word = False
            elif (not 0 <= x_loc < rows or 
                  not 0 <= y_loc < cols or 
                  board[x_loc][y_loc] not in node.children):
                  return
                
            temp_letter = board[x_loc][y_loc]
            board[x_loc][y_loc] = "."

            find_words((x_loc - 1, y_loc), node.children[temp_letter], word + temp_letter)
            find_words((x_loc + 1, y_loc), node.children[temp_letter], word + temp_letter)
            find_words((x_loc, y_loc - 1), node.children[temp_letter], word + temp_letter)
            find_words((x_loc, y_loc + 1), node.children[temp_letter], word + temp_letter)

            board[x_loc][y_loc] = temp_letter

            if len(node.children[temp_letter].children) == 0:
                del node.children[temp_letter]

        for i in range(rows):
            for j in range(cols):
                find_words((i, j), trie.root, curr_word)
        
        return matched_words
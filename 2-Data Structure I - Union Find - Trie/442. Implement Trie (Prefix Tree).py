# 442. Implement Trie (Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.

# Example
# insert("lintcode")
# search("code")
# >>> false
# startsWith("lint")
# >>> true
# startsWith("linterror")
# >>> false
# insert("linterror")
# search("lintcode)
# >>> true
# startsWith("linterror")
# >>> true
# Notice
# You may assume that all inputs are consist of lowercase letters a-z.

class TrieNode:
    
    def __init__(self):
        self.next = {}
        self.isWord = False
        
class Trie:

    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = TrieNode()
            node = node.next[letter]
        node.isWord = True
        
    def find(self, prefix):
        node = self.root
        if not node:
            return None
        for letter in prefix:
            if letter not in node.next:
                return None
            node = node.next[letter]
        return node
        

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.find(word)
        return node != None and node.isWord

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.find(prefix)
        return node != None



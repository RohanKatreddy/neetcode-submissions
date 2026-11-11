class Node:

    def __init__(self, val=None, end=False):
        self.val = val
        self.end = end
        self.adjacencyMap = defaultdict(lambda:None)

class PrefixTree:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        node = self.trie
        for letter in word:
            if letter in node.adjacencyMap:
                node = node.adjacencyMap[letter]
            else:
                newNode = Node(letter)
                node.adjacencyMap[letter] = newNode
                node = newNode
        node.end = True



    def search(self, word: str) -> bool:
        node = self.trie
        for letter in word:
            if letter not in node.adjacencyMap:
                return False
            node = node.adjacencyMap[letter]
        if node.end != True: return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for letter in prefix:
            if letter not in node.adjacencyMap:
                return False
            node = node.adjacencyMap[letter]
        return True
        
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        visited = set()
        wordSet = set(wordList)
        queue.append((beginWord, 1))

        while queue:
            word, count = queue.popleft()
            if word == endWord: return count
            if word in visited: continue
            visited.add(word)
            for i in range(len(word)):
                for chi in range(26):
                    replacement_ch = chr(ord('a') + chi)
                    newWord = word[:i] + replacement_ch + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        queue.append((newWord, count+1))
                    

        return 0
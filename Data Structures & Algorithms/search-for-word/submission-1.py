class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_lst = [ch for ch in word]

        def search(x, y, k, visited):
            if k == len(word): return True
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return False
            if (x, y) in visited: return False
            visited.add((x, y))

            found = False
            if board[x][y] == word_lst[k]:
                for newX, newY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    found = found or search(newX, newY, k+1, visited)

            visited.remove((x, y))
            return found

        found = False
        for x in range(len(board)):
            for y in range(len(board[0])):
                found = found or search(x, y, 0, set())

        return found
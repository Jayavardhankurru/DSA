class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows = len(board)
        Cols = len(board[0])
        def dfs(r, c, i):
            if len(word) == i:
                return True
            if r < 0 or c < 0 or r >= Rows or c >= Cols or board[r][c] == '#' or board[r][c] != word[i]:
                return False
            board[r][c] = '#'
            res = (dfs(r - 1, c, i + 1) or
                    dfs(r + 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        for r in range(Rows):
            for c in range(Cols):
                if dfs(r, c, 0):
                    return True
        return False
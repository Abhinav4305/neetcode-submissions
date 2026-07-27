class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
            
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"  # Mark as safe/temporary
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 🧭 Mark all border-connected 'O's as safe ('T')
        for c in range(cols):
            dfs(0, c)          # Top border
            dfs(rows - 1, c)   # Bottom border

        for r in range(rows):
            dfs(r, 0)          # Left border
            dfs(r, cols - 1)   # Right border

        # 2. 🧹 & 3. 🔄 Final pass: capture remaining 'O's to 'X', restore 'T's to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Captured!
                elif board[r][c] == "T":
                    board[r][c] = "O"  # Safe!
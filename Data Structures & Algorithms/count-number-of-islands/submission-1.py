class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cnt = 0
        
        def dfs(r, c):
            #base case if its out of bounds or is a 0 then we dont care
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS) or grid[r][c] == "0":
                return
            
            #change to 0 so we dont need to keep a visited set
            grid[r][c] = "0"

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    cnt += 1
        return cnt
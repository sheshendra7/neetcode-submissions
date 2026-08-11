class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        visit = set()
        ROWS, COLS = len(grid),len(grid[0])

        def bfs(r,c):
            q =deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if( (r,c) not in visit and
                    r in range(ROWS) and 
                     c in range(COLS) and
                     grid[r][c] == "1"):
                     q.append((r,c))
                     visit.add((r,c))
        

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    res+=1
        
        return res
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()

        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))

        while q:
            r,c, minutes_local = q.popleft()
            minutes = max(minutes, minutes_local)
            for dr,dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                if (r+dr) < 0 or r+dr >= rows or (c+dc) < 0 or c+dc>=cols:
                    continue
                
                if grid[r+dr][c+dc] == 1:
                    grid[r+dr][c+dc] = 2
                    q.append((r+dr,c+dc,minutes_local + 1))                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes

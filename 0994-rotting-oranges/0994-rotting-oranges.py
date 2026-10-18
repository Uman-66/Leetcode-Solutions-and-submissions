from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh = 0
        
        # Step 1: Scan the grid once
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))       # seed all rotten oranges
                elif grid[r][c] == 1:
                    fresh += 1                 # count fresh oranges
        
        # Step 2: No fresh oranges → already done
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 3: Multi-source BFS, one level = one minute
        while queue and fresh > 0:
            level_size = len(queue)            # all oranges rotten at this minute
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Only care about in-bounds fresh oranges
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # rot it
                        fresh -= 1             # one less fresh orange
                        queue.append((nr, nc)) # it will spread next minute
            
            minutes += 1                       # this level took one minute
        
        # Step 4: All fresh rotted? → answer, else impossible
        return minutes if fresh == 0 else -1
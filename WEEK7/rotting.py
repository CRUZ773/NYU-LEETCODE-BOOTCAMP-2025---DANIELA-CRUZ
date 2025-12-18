class Solution8:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS
        Time: O(m * n)
        Space: O(m * n)
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Find all initially rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_time = 0
        
        while queue:
            x, y, time = queue.popleft()
            max_time = max(max_time, time)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny, time + 1))
        
        return max_time if fresh == 0 else -1

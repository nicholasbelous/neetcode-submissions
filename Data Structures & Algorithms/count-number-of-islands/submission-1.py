class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1

        def search(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
                return
            else:
                grid[x][y] = "0"
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)
            
        island_count = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    island_count += 1
                    search(x,y)
        
        return island_count
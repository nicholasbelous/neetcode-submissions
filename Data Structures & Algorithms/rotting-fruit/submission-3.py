class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        time_minutes = 0
        y_len = len(grid)

        if y_len == 0:
            return -1

        x_len = len(grid[0])
        new_grid = grid
        while time_minutes >= 0:
            change_made = False
            contains_one = False
            for y in range(y_len):
                for x in range(x_len):
                    if grid[y][x] == 2:
                        if x - 1  >= 0:
                            if grid[y][x-1] == 1:
                                new_grid[y][x-1] = 2
                                change_made = True
                        if x + 1 < x_len:
                            if grid[y][x+1] == 1:
                                new_grid[y][x+1] = 2
                                change_made = True
                        if y - 1  >= 0:
                            if grid[y-1][x] == 1:
                                new_grid[y-1][x] = 2
                                change_made = True
                        if y + 1 < y_len:
                            if grid[y+1][x] == 1:
                                new_grid[y+1][x] = 2
                                change_made = True
                    if grid[y][x] == 1:
                        contains_one = True
            
            grid = new_grid

            if contains_one is False:
                print(grid)
                return time_minutes
            if change_made is False:
                return -1
            time_minutes += 1
            
        return -1
            

        
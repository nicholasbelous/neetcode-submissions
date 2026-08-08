class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        tot_y = len(boxGrid)
        tot_x = len(boxGrid[0])

        x, y = 0, 0

        new_grid = []
        for _ in range(tot_x):
            new_grid.append([])

        
        while(x < tot_x):
            while y < tot_y:
                new_grid[x].append(boxGrid[y][x])
                y += 1
            x+= 1
            y = 0
        for r in new_grid:
            r.reverse()
        for r in range(len(new_grid)):
            for c in range(len(new_grid[r])):
                row = r
                if(r == len(new_grid)-1):
                    break
                if(new_grid[r][c] == '*' or new_grid[r][c] == '.'):
                    continue
                while(row < len(new_grid) - 1):
                    if new_grid[row + 1][c] == '*':
                        break
                    if new_grid[row + 1][c] == '.':
                        new_grid[row + 1][c] = '#'
                        new_grid[r][c] = '.'
                        break
                    row += 1
        return new_grid



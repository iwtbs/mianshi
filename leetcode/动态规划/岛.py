'''
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
'''
def numIslands(self, grid) -> int:
    if not grid: return 0
    row = len(grid)
    col = len(grid[0])
    cnt = 0

    def dfs(i, j):
        grid[i][j] = "0"
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            tmp_i = i + x
            tmp_j = j + y
            if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                dfs(tmp_i, tmp_j)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                dfs(i, j)
                cnt += 1
    return cnt

'''
岛最大面积
'''
def maxAreaOfIsland(self, grid):
    row,col = len(grid),len(grid[0])
    res = 0

    def dfs(x,y):
        if x < 0 or x >= row or y < 0 or y >= col:
            return 0
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        return dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1) + 1
        
    for x in range(row):
        for y in range(col):
            if grid[x][y] == 1:
                res = max(res,dfs(x,y))
    return res
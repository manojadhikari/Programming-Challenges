'''
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer
'''

from collections import deque

def shortestCellPath(grid, sr, sc, tr, tc):
  def is_valid(r,c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
      return False

    return True

  queue = deque()
  queue.append((sr,sc,0))
  while queue:
    r, c, depth = queue.popleft()
    if r == tr and c == tc:
      return depth
    grid[r][c] = 0
    if is_valid(r-1, c):
      queue.append((r-1, c, depth+1))
    if is_valid(r+1, c):
      queue.append((r+1, c, depth+1))
    if is_valid(r, c-1):
      queue.append((r, c-1, depth+1))
    if is_valid(r, c+1):
      queue.append((r, c+1, depth+1))

  return -1

print (shortestCellPath([[1,1,1,1],[0,0,0,1],[1,1,1,1]], 0, 0, 2, 0))
'''
  def helper(r, c):

    if r == tr and c == tc:
      return 0

    if not is_valid(r,c):
      return float('inf')

    grid[r][c] = 0

    up = helper(r-1, c)
    down = helper(r+1, c)
    left = helper(r, c-1)
    right = helper(r, c+1)

    return min(min(up,down), min(left,right)) + 1

  res = helper(sr,sc)
  if res == float('inf'):
    return -1

  return res



print (shortestCellPath([[1,1,1,1],[0,0,0,1],[1,1,1,1]], 0, 0, 2, 0))

'''
'''
1, 1, 1

[1, 1, 1, 1],
[0, 0, 0, 1],
[1, 1, 1, 1]
'''

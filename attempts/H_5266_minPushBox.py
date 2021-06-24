from __future__ import annotations 
import collections 
import random 
import heapq 

# .....
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    goal = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)


        # player_loc = collections.deque()

        box_visited = set()  # loc
        box_loc = four_avail(grid, box[0], box[1], m, n)

        while box_loc:

            next_box_loc = []

            for l in box_loc:
                box_visited.add(l)
                if can_reach(grid, player[0], player[1], l[0], l[1], m, n):
                    pass



def can_reach(grid, curr_x, curr_y, goal_x, goal_y, m, n):
    if (curr_x, curr_y) == (goal_x, goal_y):
        return True

    res = False
    if curr_x-1 >= 0 and grid[curr_x-1][curr_y] == '.':
        res |= can_reach(grid, curr_x-1, curr_y, goal_x, goal_y, m, n)

    if curr_x+1 < m and grid[curr_x+1][curr_y] == '.':
        res |= can_reach(grid, curr_x+1, curr_y, goal_x, goal_y, m, n)

    if curr_y-1 >= 0 and grid[curr_x][curr_y-1] == '.':
        res |= can_reach(grid, curr_x, curr_y-1, goal_x, goal_y, m, n)

    if curr_y+1 < n and grid[curr_x][curr_y+1] == '.':
        res |= can_reach(grid, curr_x, curr_y+1, goal_x, goal_y, m, n)

    return res

def avail(grid, x, y, m, n):
    return 0 <= x < m and 0 <= y < n and grid[x][y] == '.'

def four_avail(grid, x, y, m, n):
    ret = []
    if avail(grid, x-1, y, m, n):
        ret.append( (x-1, y) )
    if avail(grid, x+1, y, m, n):
        ret.append( (x+1, y) )
    if avail(grid, x, y-1, m, n):
        ret.append( (x, y-1) )
    if avail(grid, x, y+1, m, n):
        ret.append( (x, y+1) )

    return ret

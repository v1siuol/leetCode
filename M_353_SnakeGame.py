"""
Success
Details 
Runtime: 288 ms, faster than 6.85% of Python3 online submissions for Design Snake Game.
Memory Usage: 14.6 MB, less than 73.29% of Python3 online submissions for Design Snake Game.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food = food
        self.width = width
        self.height = height
        self.score = 0
        self.body_set = set()
        self.body_queue = collections.deque()
        self.body_set.add((0,0))
        self.body_queue.append((0,0))
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        def hit_wall(point):
            x, y = point
            return 0 <= x < self.height and 0 <= y < self.width 

        def hit_body(point):
            return point in self.body_set

        def hit_food(point):
            x, y = point
            fx, fy = self.food[self.score]
            return (x, y) == (fx, fy)

        drt2loc = {'U': (-1,0), 'L': (0,-1), 'R': (0,1), 'D': (1,0)}
        ori_head_x, ori_head_y = self.body_queue[0]
        new_head_x, new_head_y = ori_head_x+drt2loc[direction][0], ori_head_y+drt2loc[direction][1]
        tail = self.body_queue[-1]
        self.body_set.remove(tail)
        
        # hit wall 
        if not hit_wall((new_head_x, new_head_y)):
            return -1
        # hit body 
        if hit_body((new_head_x, new_head_y)):
            return -1 
        # hit food

        if self.score < len(self.food) and hit_food((new_head_x, new_head_y)):
            self.score += 1
            self.body_set.add(tail)
        else:
            # normal 
            self.body_queue.pop()

        self.body_queue.appendleft((new_head_x, new_head_y))
        self.body_set.add((new_head_x, new_head_y))

        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
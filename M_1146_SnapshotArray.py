from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect



# 刚好过了5分钟5555555555 
class SnapshotArray:

    def __init__(self, length: int):
        self.lst = [{0:0} for _ in range(length)]
        print(self.lst)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.lst[index][self.snap_id] =  val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        while snap_id not in self.lst[index]:
            snap_id -= 1
        return self.lst[index][snap_id]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


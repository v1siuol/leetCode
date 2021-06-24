from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 28 ms, faster than 99.06% of Python3 online submissions for Print in Order.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Print in Order.
"""
class Foo:
    def __init__(self):
        self.locks = [threading.Lock(), threading.Lock()]
        for lock in self.locks:
            lock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.locks[0]:
            printSecond()
            self.locks[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.locks[1]:
            printThird()

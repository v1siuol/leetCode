# MAGIC

## Sort

```
# sort by key 
lst.sort(key=lambda x: (x[1], x[0]))
```

```
# sort by heap 
# Proirity queue 
min_heap = [] # heapq.heapify(lst)
heapq.heappush(min_heap, (val, -val))
heapq.heappop(min_heap)
```

```
# Merge Sort
def merge_sort(lst):
    """ Average/Worst O(n log n) Space O(n) stable
    """
    _merge_sort_between(lst, 0, len(lst)-1)

def _merge_sort_between(lst, left, right):
    # inclusive 
    if left < right:
        mid = left + (right - left) // 2
        _merge_sort_between(lst, left, mid)
        _merge_sort_between(lst, mid+1, right)
        _merge(lst, left, mid, right)

def _merge(lst, left, mid, right):
    i = left
    j = mid + 1
    tmp = []
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tmp.append(lst[i])
            i += 1
        else:
            tmp.append(lst[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else right
    tmp.extend(lst[start:end+1])
    lst[left:right+1] = tmp

def test_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
    print('True')

merge_sort_test = False
if merge_sort_test:
    test_merge_sort()
```

```
# Quick Sort
import random


def quick_sort(lst):
    # Average O(n log n) Worst O(n^2) Space O(log n) unstable
    _quick_sort_between(lst, 0, len(lst)-1)

def _quick_sort_between(lst, left, right):
    if left < right:
        pvt = random.randint(left, right)  # inclusive
        lst[left], lst[pvt] = lst[pvt], lst[left]

        pivot = _partition(lst, left, right)
        _quick_sort_between(lst, left, pivot-1)
        _quick_sort_between(lst, pivot+1, right)

def _partition(lst, left, right):
    pivot = lst[left]
    j = left
    for i in range(left+1, right+1):
        if lst[i] <= pivot:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j

def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
    print('True')

quick_sort_test = False
if quick_sort_test:
    test_quick_sort()

```

## Math
```
# 取末位 反着顺序
while num != 0:
	num %= 10
	num //= 10
```

## MISC
```
# 合并区间 sort 然后比头尾
```

## STRING
```
# string window
# 先设总+小counter 后start=end=0 一直跑条件然后缩条件循环
```


## BINARY SEARCH
```
left = 0
right = len(nums) - 1
while left <= right:
	mid = (left + right) // 2  # mid = left + (right - left) // 2
	if target < mid:
		right = mid - 1
	elif target > mid:
		left = mid + 1
	else:
		return mid 
return -1 
```

## UNION FIND 
```
# 每次union的是O(log n)，path compression优化是接近O(1)，但有n^2次unoin find，总算法是O(n^2)。
"""
https://leetcode.com/problems/friend-circles/
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # union find 
        n = len(M)
        count = n
        roots = [i for i in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                # upper right matrix / not include diagonals 
                if M[i][j] == 1:
                    x = find(roots, i)
                    y = find(roots, j)
                    if x != y:
                        roots[x] = y
                        count -=1
        return count

def find(roots, id):
    while roots[id] != id:
        roots[id] = roots[roots[id]]  # path compression 
        id = roots[id]
    return id

s = Solution()
s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])  # 2
s.findCircleNum([[1,1,0],[1,1,1],[0,1,1]])  # 1
```

## SQRT
```
牛顿法 Newton's Method 快速开方
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x//r) // 2
        return r
```

## Dynamic Programming
```
gg
状态转移方程
```

## Single Linked List
```
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = Node(None)  # fake head

    def append_to_tail(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def pop_tail(self):
        curr = self.head
        while curr.next:
            if not curr.next.next:
                curr.next = None
                break
            curr = curr.next

    def print(self):
        curr = self.head.next
        print('LinkedList: ', end='')
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print()

    def is_empty(self):
        return self.head.next is None


single_linked_link_test = False
if single_linked_link_test:
    s = SingleLinkedList()
    s.append_to_tail(1)
    print('Empty? ', s.is_empty())
    s.append_to_tail(2)
    s.append_to_tail(3)
    s.print()
    s.pop_tail()
    s.pop_tail()
    s.pop_tail()
    s.print()
    print('Empty? ', s.is_empty())
```

## Double Linked List
```
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, val):
        new_node = Node(val)
        prev_head = self.head.next
        prev_head.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = prev_head

    def append_to_tail(self, val):
        new_node = Node(val)
        prev_tail = self.tail.prev
        prev_tail.next = new_node
        self.tail.prev = new_node
        new_node.prev = prev_tail
        new_node.next = self.tail

    def pop_head(self):
        if self.head.next.next:
            new_head = self.head.next.next
            self.head.next = new_head
            new_head.prev = self.head

    def pop_tail(self):
        if self.tail.prev.prev:
            new_tail = self.tail.prev.prev
            self.tail.prev = new_tail
            new_tail.next = self.tail

    def print(self):
        curr = self.head.next
        print('LinkedList: ', end='')
        while curr:
            print(curr.val, end=' -> ')
            curr = curr.next
        print()
        curr = self.tail.prev
        while curr:
            print(curr.val, end=' <- ')
            curr = curr.prev
        print()

    def is_empty(self):
        return self.head.next.next is None


double_linked_link_test = False
if double_linked_link_test:
    s = DoubleLinkedList()
    s.add_to_head(1)
    print('Empty? ', s.is_empty())
    s.print()
    s.pop_tail()
    print('Empty? ', s.is_empty())
    s.print()
    s.append_to_tail(1)
    s.add_to_head(2)
    s.pop_head()
    s.print()
```

## Trie
```
import collections


class Node:

    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return curr.is_word

trie_test = False
if trie_test:
    t = Trie()
    t.insert('abc')
    print(t.search('abc'))  # True
    print(t.search('a'))
    print(t.search('b'))
    print(t.search('abcd'))

```

## Tree
未测试
```
# inorder
# preorder 
# postorder

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    if root:
        in_order(root.left):
        print(root.val)
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        pre_order(root.left)
        pre_order(root.right)
        print(root.val)
```

## Stack
未测试
```
class MyStack:

    def __init__(self):
        self.stack = []

    def reverse(self):
        # bug 
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self._reverse_helper(temp)

    def _reverse_helper(self, val):
        """insert at bottom
        """
        if self.is_empty():
            self.append(temp)
        else:
            temp = self.pop()
            self._reverse_helper(val)
            self.append(temp)

    def sort(self):
        pass

    def _sort_helper(self):
        pass

    def push(self, val):
        self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.pop()

    def is_empty(self):
        return len(self.stack) == 0

```

## Kth largest
```
import heapq


def kth_largest(lst, K):
    """min_heap
    O(N log k) time complexity O(k) space complexity 
    """
    min_heap = []
    capacity = 0
    for num in nums:
        heapq.heappush(min_heap, num)
        capacity += 1

        if capacity > k:
            heapq.heappop(min_heap)

    return min_heap[0]
```

## K largest
未测试
```
import heapq


def k_largest(lst, K):
    """min_heap
    """
    min_heap = []
    capacity = 0
    for num in nums:
        heapq.heappush(min_heap, num)
        capacity += 1

        if capacity > k:
            heapq.heappop(min_heap)

    ret = []
    while min_heap:
        ret.append(heapq.heappop(min_heap))

    return ret[::-1]
```
"""
Success
Details 
Runtime: 304 ms, faster than 48.83% of Python3 online submissions for Sudoku Solver.
Memory Usage: 13.6 MB, less than 5.31% of Python3 online submissions for Sudoku Solver.
"""
from __future__ import annotations 
from collections import deque
from copy import deepcopy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        s = Sudoku(read_board(board))
        s.infer_with_guessing()
        for key, val in s.board.items():
            board[key[0]][key[1]] = str(val.pop())


def read_board(_board):
    board = {}
    for row, line in enumerate(_board):     
        for col, char in enumerate(line):
            if char == '.':
                sel_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                sel_set = set([int(char)])
            board[(row, col)] = sel_set
    return board

def sudoku_cells():
    return [(i, j) for i in range(9) for j in range(9)]

def sudoku_arcs():
    # cannot be same value
    # horizen 
    # O(n^2) manually O1
    arc_set = set()

    # col vertical 648
    for k in range(9):  # row num
        for i in range(9):  # first loc
            for j in range(i+1, 9):  # second loc
                arc_set.add(((k, i), (k, j)))
                arc_set.add(((k, j), (k, i)))

    # row herizon 648 
    for k in range(9):  # col num
        for i in range(9):  # first loc
            for j in range(i+1, 9):  # second loc
                arc_set.add(((i, k), (j, k)))
                arc_set.add(((j, k), (i, k)))

    # small square 36 * 9 = 324 
    x_index_int = 0
    y_index_int = 0
    for i in range(9):
        for j in range(9):
            # 4x points
            gap_int = 3
            if i >=6:
                x_index_int = 2
            elif i >=3:
                x_index_int = 1
            else:
                x_index_int = 0

            if j >=6:
                y_index_int = 2
            elif j >=3:
                y_index_int = 1
            else:
                y_index_int = 0

            arc_set.add( ( ( (i+1)%3 + x_index_int*gap_int, (j+1)%3 + y_index_int*gap_int), (i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int) ) )
            arc_set.add( ( ( (i+1)%3 + x_index_int*gap_int, (j+2)%3 + y_index_int*gap_int), (i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int) ) )
            arc_set.add( ( ( (i+2)%3 + x_index_int*gap_int, (j+1)%3 + y_index_int*gap_int), (i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int) ) )
            arc_set.add( ( ( (i+2)%3 + x_index_int*gap_int, (j+2)%3 + y_index_int*gap_int), (i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int) ) )
            arc_set.add( ( ( i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int), ( (i+1)%3 + x_index_int*gap_int, (j+1)%3 + y_index_int*gap_int),  ) )
            arc_set.add( ( ( i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int), ( (i+1)%3 + x_index_int*gap_int, (j+2)%3 + y_index_int*gap_int),  ) )
            arc_set.add( ( ( i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int), ( (i+2)%3 + x_index_int*gap_int, (j+1)%3 + y_index_int*gap_int),  ) )
            arc_set.add( ( ( i%3 + x_index_int*gap_int, j%3 + y_index_int*gap_int), ( (i+2)%3 + x_index_int*gap_int, (j+2)%3 + y_index_int*gap_int),  ) )

    return arc_set # 1620


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs() 

    def __init__(self, board):
        self.arcs_queue = Sudoku.ARCS.copy()  
        self.board = board

    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        target_set = self.board[cell2]
        if len(target_set) != 1:
            return False
        target_num_int = next(iter(target_set))
        if target_num_int in self.board[cell1]:
            self.board[cell1].remove(target_num_int)
            return True
        else:
            return False

    def _get_board_str_for_debug(self):
        ret_board_str = ''
        for cell in Sudoku.CELLS:
            if len(self.board[cell]) != 1:
                ret_board_str += '*'
            else:
                ret_board_str += str(next(iter(self.board[cell])))
        
        return ret_board_str


    def _neighbors_x_i_except_x_j(self, x_i, x_j):
        row, col = x_i
        col_nei = [(i, col) for i in range(9) if i != row]
        row_nei = [(row, j) for j in range(9) if j != col]

        gap_int = 3
        if row >=6:
            x_index_int = 2
        elif row >=3:
            x_index_int = 1
        else:
            x_index_int = 0

        if col >=6:
            y_index_int = 2
        elif col >=3:
            y_index_int = 1
        else:
            y_index_int = 0

        sqr_nei = []
        sqr_nei.append( ( ( (row+1)%3 + x_index_int*gap_int, (col+1)%3 + y_index_int*gap_int) ) )
        sqr_nei.append( ( ( (row+1)%3 + x_index_int*gap_int, (col+2)%3 + y_index_int*gap_int) ) )
        sqr_nei.append( ( ( (row+2)%3 + x_index_int*gap_int, (col+1)%3 + y_index_int*gap_int) ) )
        sqr_nei.append( ( ( (row+2)%3 + x_index_int*gap_int, (col+2)%3 + y_index_int*gap_int) ) )

        nei_lst = col_nei+row_nei+sqr_nei
        nei_lst.remove((x_j))
        return nei_lst  # 20 neighbors - 1

    def infer_ac3(self):
        # CELLS <-> X
        # self.board <-> D
        while len(self.arcs_queue) > 0:
            x_i, x_j = next(iter(self.arcs_queue))
            self.arcs_queue.remove((x_i, x_j))
            
            if self.remove_inconsistent_values(x_i, x_j):
                for x_k in self._neighbors_x_i_except_x_j(x_i, x_j):
                    self.arcs_queue.add((x_k, x_i))
        return True

    def _is_solved(self):
        """ test len(domain)==1, ignored value inside"""
        for cell in self.board:
            domain_set = self.get_values(cell)
            if len(domain_set) != 1:  
                return False
        return True

    def _get_domain_set(self, square_cells):
        ret_num_set = set()
        for i in square_cells:
            ret_num_set.update(self.get_values(i))
        return ret_num_set


    def _get_square_nei_cell_set(self, cell):
        ret_set = set()
        row = cell[0]
        col = cell[1]
        gap_int = 3
        if row >=6:
            x_index_int = 2
        elif row >=3:
            x_index_int = 1
        else:
            x_index_int = 0

        if col >=6:
            y_index_int = 2
        elif col >=3:
            y_index_int = 1
        else:
            y_index_int = 0

        for i in range(3):
            for j in range(3):
                ret_set.add((x_index_int*gap_int+i, y_index_int*gap_int+j))
        ret_set.remove(cell)
        return ret_set

    def _get_horizotal_nei_cell_set(self, x_i):
        row, col = x_i
        row_nei = [(row, j) for j in range(9) if j != col]
        return row_nei

    def _get_vertical_nei_cell_set(self, x_i):
        row = x_i[0]
        col = x_i[1]
        col_nei = [(i, col) for i in range(9) if i != row]
        return col_nei

    def _hor_ver_infer_helper(self):
        is_revised = False
        for curr_cell in Sudoku.CELLS:
            domain_set = self.get_values(curr_cell)
            if len(domain_set) != 1:
                # look for inference
                for num in domain_set:
                    union_set = self._get_square_nei_cell_set(curr_cell)
                    union_domain_set = self._get_domain_set(union_set)
                    if num not in union_domain_set:
                        # found
                        self.board[curr_cell] = {num}

                        for x_k in self._get_horizotal_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))

                        for x_k in self._get_vertical_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))
                        is_revised = True
                        break

                    # horizontal other check
                    union_set = self._get_horizotal_nei_cell_set(curr_cell)
                    union_domain_set = self._get_domain_set(union_set)
                    if num not in union_domain_set:
                        # found
                        self.board[curr_cell] = {num}

                        for x_k in self._get_square_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))

                        for x_k in self._get_vertical_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))
                        is_revised = True
                        break

                    # veritcal other check
                    union_set = self._get_vertical_nei_cell_set(curr_cell)
                    union_domain_set = self._get_domain_set(union_set)
                    if num not in union_domain_set:
                        # found
                        self.board[curr_cell] = {num}

                        for x_k in self._get_horizotal_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))

                        for x_k in self._get_square_nei_cell_set(curr_cell):
                            self.arcs_queue.add((x_k, curr_cell))
                        is_revised = True
                        break

        return is_revised

    def infer_improved(self):
        self.infer_ac3()
        while self._hor_ver_infer_helper(): 
            self.infer_ac3()
        return True

    def _successors(self):
        for cell in Sudoku.CELLS:
            domain_set = self.board[cell]
            if len(domain_set) > 1:
                arcs_queue = set()
                for x_k in self._get_horizotal_nei_cell_set(cell):
                    arcs_queue.add((x_k, cell))
                for x_k in self._get_vertical_nei_cell_set(cell):
                    arcs_queue.add((x_k, cell))
                for x_k in self._get_square_nei_cell_set(cell):
                    arcs_queue.add((x_k, cell))

                for guess_value in domain_set:
                    new_sudoku = deepcopy(self)
                    new_sudoku.arcs_queue = arcs_queue.copy()
                    new_sudoku.board[cell] = {guess_value}  # set
                    yield new_sudoku

                break

    def infer_with_guessing(self):
        self.infer_improved()
        frontier = deque()
        frontier.append(self)
        # no dfs here 
        while len(frontier) > 0:
            next_sudoku = frontier.pop()
            for new_sudoku in next_sudoku._successors():
                new_sudoku.infer_improved()
                if new_sudoku._is_solved():
                    self.board = new_sudoku.board
                    return True
                else:
                    frontier.append(new_sudoku)

        # care not solve 
        return False  















s = Solution()


lst = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
s.solveSudoku(lst)
print(lst)  




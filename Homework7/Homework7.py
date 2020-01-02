import math
import copy
import time

def sudoku_cells():
    cells = []
    for row in range(9):
        for col in range(9):
            cells.append((row, col))
    return cells

def sudoku_arcs():
    arcs = []
    for row in range(9):
        for col in range(9):
            #iterate through each cell, now find cells that it cannot match with(excluding itself)
            #add in all cells in the same row in column
            for x in range(9):
                if x != row:
                    arcs.append(((row, col), (x, col)))
                if x != col:
                    arcs.append(((row, col), (row, x)))
            #add in all cells in the same box(don't double count ones in same row/col)
            boxRow = math.floor(row/3)
            boxCol = math.floor(col/3)
            for row2 in range(boxRow * 3, (boxRow + 1) * 3):
                for col2 in range(boxCol * 3, (boxCol + 1) * 3):
                    if row2 != row and col2 != col:
                        arcs.append(((row, col), (row2, col2)))
    return arcs

def read_board(path):
    lines = []
    board = {}
    with open(path, "r") as txt:
        lines = txt.readlines()
    for row, line in enumerate(lines):
        for col in range(len(line)):
            if col < 9:
                digit = line[col]
                if line[col] != "*":
                    digit = int(line[col])
                board[(row, col)] = set([digit])
    return board

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        self.Map = board
        self.Neighbors = {}
        self.UnsolvedCells = set()
        for cell in self.CELLS:
            if self.Map[cell] == set(["*"]):
                self.Map[cell] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                self.UnsolvedCells.add(cell)

        for arc in self.ARCS:
            if arc[1] not in self.Neighbors:
                self.Neighbors[arc[1]] = []
            self.Neighbors[arc[1]].append(arc[0])

    def get_values(self, cell):
        return [self.Map[cell]]

    def remove_inconsistent_values(self, cell1, cell2):
        if cell2 in self.Neighbors[cell1]:
            #there are values to be removed potentially
            if len(self.Map[cell2]) == 1:
                digit = next(iter(self.Map[cell2]))
                if digit in self.Map[cell1]:
                    self.Map[cell1].remove(digit)
                    return True
        return False

    def infer_ac3(self):
        arclist = copy.deepcopy(self.ARCS)
        for arc in arclist:
            if self.remove_inconsistent_values(arc[0], arc[1]):
                #add all arcs pointing to arc[0] to arclist
                for x in self.Neighbors[arc[0]]:
                    arclist.append((x, arc[0]))

    def infer_blocks(self):
        for cell in self.CELLS:
            if len(self.Map[cell]) > 1:
                row = cell[0]
                col = cell[1]
                digits = copy.deepcopy(self.Map[cell])
                boxRow = math.floor(row/3)
                boxCol = math.floor(col/3)
                for row2 in range(boxRow * 3, (boxRow + 1) * 3):
                    for col2 in range(boxCol * 3, (boxCol + 1) * 3):
                        if row2 != row or col2 != col:
                            #different cells in the same block
                            digits = digits - self.Map[(row2, col2)]
                #if cell has a possible solution still, that is the solution
                if len(digits) > 0:
                    self.Map[cell] = set([list(digits)[0]])
                self.infer_ac3()

    def infer_rowscols(self):
        for cell in self.CELLS:
            if len(self.Map[cell]) > 1:
                row = cell[0]
                col = cell[1]
                digitsRow = copy.deepcopy(self.Map[cell])
                digitsCol = copy.deepcopy(self.Map[cell])
                for i in range(9):
                    if i != row:
                        digitsCol = digitsCol - self.Map[(i, col)]
                    if i != col:
                        digitsRow = digitsRow - self.Map[(row, i)]
                if len(digitsRow) > 0:
                    self.Map[cell] = set([list(digitsRow)[0]])
                if len(digitsCol) > 0:
                    self.Map[cell] = set([list(digitsCol)[0]])
                self.infer_ac3()

    def infer_improved(self):
        self.infer_ac3()
        #check cells in each block to see if there are any digits that can only be placed in one cell
        self.infer_blocks()
        #check cells in each row/column to see if there are any digits that can only be placed in one cell
        self.infer_rowscols()

        #check cells in each block to see if there are any digits that can only be placed in one row or column
        for block in range(9):
            boxRow = math.floor(block/3)
            boxCol = block - boxRow * 3
            for i in range(3):
                col = boxCol * 3 + i
                row = boxRow * 3 + i
                digitsRow = []
                digitsNotRow = []
                digitsCol = []
                digitsNotCol = []
                if i == 0:
                    digitsCol = list(self.Map[row, col]) + list(self.Map[row + 1, col]) + list(self.Map[row + 2, col])
                    digitsRow = list(self.Map[row, col]) + list(self.Map[row, col + 1]) + list(self.Map[row, col + 2])
                    digitsNotCol = list(self.Map[row, col + 1]) + list(self.Map[row + 1, col + 1]) + list(self.Map[row + 2, col + 1]) + list(self.Map[row, col + 2]) + list(self.Map[row + 1, col + 2]) + list(self.Map[row + 2, col + 2])
                    digitsNotRow = list(self.Map[row + 1, col]) + list(self.Map[row + 1, col + 1]) + list(self.Map[row + 1, col + 2]) + list(self.Map[row + 2, col]) + list(self.Map[row + 2, col + 1]) + list(self.Map[row + 2, col + 2])
                elif i == 1:
                    digitsCol = list(self.Map[row, col]) + list(self.Map[row + 1, col]) + list(self.Map[row - 1, col])
                    digitsRow = list(self.Map[row, col]) + list(self.Map[row, col + 1]) + list(self.Map[row, col - 1])
                    digitsNotCol = list(self.Map[row, col + 1]) + list(self.Map[row + 1, col + 1]) + list(self.Map[row - 1, col + 1]) + list(self.Map[row, col - 1]) + list(self.Map[row + 1, col - 1]) + list(self.Map[row - 1, col - 1])
                    digitsNotRow = list(self.Map[row + 1, col]) + list(self.Map[row + 1, col + 1]) + list(self.Map[row + 1, col - 1]) + list(self.Map[row - 1, col]) + list(self.Map[row - 1, col + 1]) + list(self.Map[row - 1, col - 1])
                elif i == 2:
                    digitsCol = list(self.Map[row, col]) + list(self.Map[row - 1, col]) + list(self.Map[row - 2, col])
                    digitsRow = list(self.Map[row, col]) + list(self.Map[row, col - 1]) + list(self.Map[row, col - 2])
                    digitsNotCol = list(self.Map[row, col - 1]) + list(self.Map[row - 1, col - 1]) + list(self.Map[row - 2, col - 1]) + list(self.Map[row, col - 2]) + list(self.Map[row - 1, col - 2]) + list(self.Map[row - 2, col - 2])
                    digitsNotRow = list(self.Map[row - 1, col]) + list(self.Map[row - 1, col - 1]) + list(self.Map[row - 1, col - 2]) + list(self.Map[row - 2, col]) + list(self.Map[row - 2, col - 1]) + list(self.Map[row - 2, col - 2])
                
                digitsRow = set(digitsRow)
                digitsCol = set(digitsCol)
                digitsNotRow = set(digitsNotRow)
                digitsNotCol = set(digitsNotCol)
                digitsRow = digitsRow - digitsNotRow
                digitsCol = digitsCol - digitsNotCol
                for x in range(9):
                    if x < boxCol * 3 or x >= (boxCol + 1) * 3:
                        self.Map[(row, x)] = self.Map[(row, x)] - digitsRow
                    if x < boxRow * 3 or x >= (boxRow + 1) * 3:
                        self.Map[(x, col)] = self.Map[(x, col)] - digitsCol

        self.infer_blocks()

    
    def is_valid(self):
        for cell in self.CELLS:
            if len(self.Map[cell]) == 0:
                return False
        return True

    def is_solved(self):
        for cell in self.CELLS:
            if len(self.Map[cell]) != 1:
                return False
        return True

    def infer_with_guessing(self):
        self.infer_improved()

        def guess(self):
            for cell in self.CELLS:
                if len(self.Map[cell]) > 1:
                    for digit in self.Map[cell]:
                        map = copy.deepcopy(self.Map)
                        self.Map[cell] = set([digit])
                        self.infer_improved()
                        if self.is_solved():
                            return
                        if self.is_valid():
                            guess(self)
                        if self.is_solved():
                            return
                        self.Map = map

        guess(self)
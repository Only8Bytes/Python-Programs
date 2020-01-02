import random
import math

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    return int(math.factorial(n*n)/(math.factorial(n)*math.factorial(n*n - n)))

def num_placements_one_per_row(n):
    return int(math.factorial(n))

def n_queens_valid(board):
    checked = []
    for x in board:
        if x in checked:
            return False
        else:
            checked.append(x)
    places = []
    for i, x in enumerate(board):
        places.append((i, x))
    for i, x in enumerate(places):
        for y in places[i + 1:]:
            if abs((y[1] - x[1])/(y[0] - x[0])) == 1:
                return False
    return True

def n_queens_solutions(n):
    DFSpaths = []
    stack = []
    def DFS():
        if len(stack) == n:
            DFSpaths.append(stack[:])
            stack.pop()
        else:
            for i in range(n):
                if not i in stack:
                    stack.append(i)
                    if n_queens_valid(stack):
                        DFS()
                    else:
                        stack.pop()
            if len(stack) > 0:
                stack.pop()

    DFS()
    for v in DFSpaths:
        yield v

############################################################
# Section 2: Lights Out
############################################################

def makeTuple(source):
    return tuple(map(tuple, source))

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.Board = board
        self.PreviousNode = None
        pass

    def get_board(self):
        return self.Board

    def perform_move(self, row, col):
        self.Board[row][col] = not self.Board[row][col]
        if row > 0:
            self.Board[row - 1][col] = not self.Board[row - 1][col]
        if row < len(self.Board) - 1:
            self.Board[row + 1][col] = not self.Board[row + 1][col]
        if col > 0:
            self.Board[row][col - 1] = not self.Board[row][col - 1]
        if col < len(self.Board[0]) - 1:
            self.Board[row][col + 1] = not self.Board[row][col + 1]
        pass

    def scramble(self):
        for x in range(len(self.Board)):
            for y in range(len(self.Board[0])):
                if random.random() < .5:
                    self.perform_move(x, y)
        pass

    def is_solved(self):
        for x in range(len(self.Board)):
            for y in range(len(self.Board[0])):
                if self.Board[x][y]:
                    return False
        return True

    def copy(self):
        newBoard = [[col for col in row] for row in self.get_board()]
        return LightsOutPuzzle(newBoard)

    def successors(self):
        for x in range(len(self.Board)):
            for y in range(len(self.Board[0])):
                newBoard = self.copy()
                newBoard.perform_move(x, y)
                yield ((x, y), newBoard.get_board())
        pass

    def find_solution(self):
        #BFS function
        def BFS(self):
            #create a dictionary to define what nodes(given by board) have been visited, add source to queue and marked as visited
            visited = {}
            queue = [self]
            visited[makeTuple(self.get_board())] = True
            #iterate through every board in the queue until it is exhausted
            while len(queue) > 0:
                currentNode = queue.pop(0)
                if currentNode.is_solved():
                    path = []
                    while currentNode.PreviousNode != None:
                        path.insert(0, currentNode.PreviousNode[1])
                        currentNode = currentNode.PreviousNode[0]
                    return path
                #iterate over every square to generate every possible next board
                for x in range(len(currentNode.get_board())):
                    for y in range(len(currentNode.get_board()[0])):
                        copyNode = currentNode.copy()
                        copyNode.perform_move(x, y)
                        if not makeTuple(copyNode.get_board()) in visited:
                            queue.append(copyNode)
                            visited[makeTuple(copyNode.get_board())] = True
                            copyNode.PreviousNode = (currentNode, (x, y))
            return None

        return BFS(self)

def create_puzzle(rows, cols):
    board = [[False] * cols for i in range(rows)]
    return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################

class DiskPuzzle(object):
    def __init__(self, puzzle):
        self.PreviousNode = None
        self.Puzzle = puzzle

    def copy(self):
        newPuzzle = [n for n in self.Puzzle]
        return DiskPuzzle(newPuzzle)
    
    def is_solved(self):
        DiskFound = False
        for x in self.Puzzle:
            if x == True:
                DiskFound = True
            elif DiskFound:
                return False
        return True

    def is_distinct_solved(self):
       return self.Puzzle == sorted(self.Puzzle)

    def get_puzzle(self):
        return self.Puzzle

    def perform_swap(self, a, b):
        if self.Puzzle[a] != self.Puzzle[b] and (a - b == 1 or a - b == -1):
            temp = self.Puzzle[a]
            self.Puzzle[a] = self.Puzzle[b]
            self.Puzzle[b] = temp
        
    def perform_hop(self, a, b):
        if self.Puzzle[a] != self.Puzzle[b] and (a - b == 2 or a - b == -2):
            temp = self.Puzzle[a]
            self.Puzzle[a] = self.Puzzle[b]
            self.Puzzle[b] = temp

    def is_valid_move(self, a, b):
        return a >= 0 and a <= len(self.Puzzle) - 1 and b >= 0 and b <= len(self.Puzzle) - 1 and self.Puzzle[a] != self.Puzzle[b] and (a - b == 1 or a - b == -1 or a - b == 2 or a - b == -2)

def solve_identical_disks(length, n):
    def create_puzzle(length, n):
        puzzle = [False] * length
        for i in range(n):
            puzzle[i] = True
        return DiskPuzzle(puzzle)

    def BFS(source):
        visited = [source.get_puzzle()]
        queue = [source]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            if currentNode.is_solved():
                path = []
                while currentNode.PreviousNode != None:
                    path.insert(0, currentNode.PreviousNode[1])
                    currentNode = currentNode.PreviousNode[0]
                return path
            #hop forward
            for j in range(len(currentNode.get_puzzle())):
                i = j - 2
                if currentNode.is_valid_move(i, i + 2):
                    copyNode = currentNode.copy()
                    copyNode.perform_hop(i, i + 2)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i + 2))
            #hop backward
            for i in range(2, len(currentNode.get_puzzle())):
                if currentNode.is_valid_move(i, i - 2):
                    copyNode = currentNode.copy()
                    copyNode.perform_hop(i, i - 2)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i - 2))
            #move forward
            for j in range(len(currentNode.get_puzzle())):
                i = j - 1
                if currentNode.is_valid_move(i, i + 1):
                    copyNode = currentNode.copy()
                    copyNode.perform_swap(i, i + 1)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i + 1))
            #move backward
            for i in range(1, len(currentNode.get_puzzle())):
                if currentNode.is_valid_move(i, i - 1):
                    copyNode = currentNode.copy()
                    copyNode.perform_swap(i, i - 1)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i - 1))


    return BFS(create_puzzle(length, n))

def solve_distinct_disks(length, n):
    def create_puzzle(length, n):
        puzzle = [0] * length
        for i in range(n):
            puzzle[i] = n - i
        return DiskPuzzle(puzzle)

    def BFS(source):
        visited = [source.get_puzzle()]
        queue = [source]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            if currentNode.is_distinct_solved():
                path = []
                while currentNode.PreviousNode != None:
                    path.insert(0, currentNode.PreviousNode[1])
                    currentNode = currentNode.PreviousNode[0]
                return path
            #hop forward
            for j in range(len(currentNode.get_puzzle())):
                i = j - 2
                if currentNode.is_valid_move(i, i + 2):
                    copyNode = currentNode.copy()
                    copyNode.perform_hop(i, i + 2)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i + 2))
            #hop backward
            for i in range(2, len(currentNode.get_puzzle())):
                if currentNode.is_valid_move(i, i - 2):
                    copyNode = currentNode.copy()
                    copyNode.perform_hop(i, i - 2)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i - 2))
            #move forward
            for j in range(len(currentNode.get_puzzle())):
                i = j - 1
                if currentNode.is_valid_move(i, i + 1):
                    copyNode = currentNode.copy()
                    copyNode.perform_swap(i, i + 1)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i + 1))
            #move backward
            for i in range(1, len(currentNode.get_puzzle())):
                if currentNode.is_valid_move(i, i - 1):
                    copyNode = currentNode.copy()
                    copyNode.perform_swap(i, i - 1)
                    if not copyNode.get_puzzle() in visited:
                        queue.append(copyNode)
                        visited.append(copyNode.get_puzzle())
                        copyNode.PreviousNode = (currentNode, (i, i - 1))

    return BFS(create_puzzle(length, n))

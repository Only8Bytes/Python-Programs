from graphics import *
import random
import time

cellList = []
startCell = None
goalCell = None
win = None
padding = 50
cellSize = 20
lineThickness = 2

class Cell:
    Goal = False
    Start = False
    X = None
    Y = None
    wallNorth = True
    wallSouth = True
    wallEast = True
    wallWest = True

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def SetStart(self):
        self.Start = True
        self.wallWest = False
        global startCell
        startCell = self

    def SetGoal(self):
        self.Goal = True
        self.wallEast = False
        global goalCell
        goalCell = self

    def GetNeighbors(self):
        neighbors = []
        if self.X > 0:
            neighbors.append(cellList[self.Y][self.X - 1])
        if self.Y > 0:
            neighbors.append(cellList[self.Y - 1][self.X])
        if self.X < len(cellList[0]) - 1:
            neighbors.append(cellList[self.Y][self.X + 1])
        if self.Y < len(cellList) - 1:
            neighbors.append(cellList[self.Y + 1][self.X])
        
        random.shuffle(neighbors)
        return neighbors

def populateGrid(sizeX, sizeY):
    for i in range(sizeY):
        cellList.append([])
        for j in range(sizeX):
            cellList[i].append(Cell(j, i))

    cellList[random.randrange(sizeY)][0].SetStart()
    cellList[random.randrange(sizeY)][sizeX - 1].SetGoal()

def createPath():
    visitedCells = []
    cellStack = []

    cellStack.append(startCell)
    visitedCells.append(startCell)
    while len(cellStack) > 0:
        cell = cellStack.pop()
        for neighbor in cell.GetNeighbors():
            if neighbor not in visitedCells:
                cellStack.append(cell)
                
                if cell.X < neighbor.X:
                    cell.wallEast = False
                    neighbor.wallWest = False
                if cell.X > neighbor.X:
                    cell.wallWest = False
                    neighbor.wallEast = False
                if cell.Y < neighbor.Y:
                    cell.wallSouth = False
                    neighbor.wallNorth = False
                if cell.Y > neighbor.Y:
                    cell.wallNorth = False
                    neighbor.wallSouth = False

                visitedCells.append(neighbor)
                cellStack.append(neighbor)
                break

def drawMaze():
    global win

    def drawLine(p1, p2):
        line = Line(p1, p2)
        line.setWidth(lineThickness)
        line.draw(win)

    win = GraphWin("Maze", padding * 2 + len(cellList[0]) * cellSize, padding * 2 + len(cellList) * cellSize)

    for i, row in enumerate(cellList):
        for j, cell in enumerate(row):
            cellX = padding + j * cellSize
            cellY = padding + i * cellSize

            if cell.wallNorth:
                drawLine(Point(cellX - lineThickness/2, cellY), Point(cellX + cellSize + lineThickness/2, cellY))
            if cell.wallSouth:
                drawLine(Point(cellX - lineThickness/2, cellY + cellSize), Point(cellX + cellSize + lineThickness/2, cellY + cellSize))
            if cell.wallEast:
                drawLine(Point(cellX + cellSize, cellY - lineThickness/2), Point(cellX + cellSize, cellY + cellSize + lineThickness/2))
            if cell.wallWest:
                drawLine(Point(cellX, cellY - lineThickness/2), Point(cellX, cellY + cellSize + lineThickness/2))

def GenerateMaze(x, y):
    populateGrid(x, y)
    createPath()
    drawMaze()

def SolveMaze():
    def DFS(path, visited, node):
        if node not in visited:
            #time.sleep(.1)
            rect = Rectangle(Point(padding + node.X * cellSize + 5, padding + node.Y * cellSize + 5), Point(padding + node.X * cellSize + cellSize - 5, padding + node.Y * cellSize + cellSize - 5))
            rect.setFill("green")
            rect.setWidth(0)
            rect.draw(win)
            path.append(node)
            visited.append(node)
            if node != goalCell:
                if all(cell in visited for cell in node.GetNeighbors()):
                    #time.sleep(.1)
                    path.pop()
                    rect.setFill("red")
                else:
                    for neighbor in node.GetNeighbors():
                        if path[-1] == goalCell:
                            break
                        if (neighbor.X > node.X and not node.wallEast) or (neighbor.X < node.X and not node.wallWest) or (neighbor.Y > node.Y and not node.wallSouth) or (neighbor.Y < node.Y and not node.wallNorth):
                            DFS(path, visited, neighbor)
                    if path[-1] != goalCell:
                        #time.sleep(.1)
                        path.pop()
                        rect.setFill("red")
                        
            return path

    DFS([], [], startCell)


GenerateMaze(20, 20)
time.sleep(3)
SolveMaze()
win.getMouse()
win.close()
import pygame
import random
import math
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('arial', 30)
    LARGE_FONT = pygame.font.SysFont('arial', 40)
    SIDE_BUFFER = 100
    TOP_BUFFER = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.setList(lst)

    def setList(self, lst):
        self.lst = lst
        self.maxValue = max(lst)
        self.minValue = min(lst)

        self.blockWidth = round((self.width - self.SIDE_BUFFER) / len(lst))
        self.blockHeight = math.floor((self.height - self.TOP_BUFFER) / (self.maxValue - self.minValue))
        self.startx = self.SIDE_BUFFER // 2

def generateStartingList(n, minVal, maxVal):
    lst = []
    for _ in range(n):
        val = random.randint(minVal, maxVal)
        lst.append(val)
    return lst

def draw(drawInfo, algoName, ascending):
    drawInfo.window.fill(drawInfo.BACKGROUND_COLOR)

    title = drawInfo.LARGE_FONT.render(f"{algoName} - {'Ascending' if ascending else 'Descending'}", 1, drawInfo.GREEN)
    drawInfo.window.blit(title, (drawInfo.width / 2 - title.get_width() / 2, 5))

    controls = drawInfo.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, drawInfo.BLACK)
    drawInfo.window.blit(controls, (drawInfo.width / 2 - controls.get_width()/2, 45))

    sorting = drawInfo.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, drawInfo.BLACK)
    drawInfo.window.blit(sorting, (drawInfo.width / 2 - sorting.get_width() / 2, 75))

    drawList(drawInfo)
    pygame.display.update()

def drawList(drawInfo, colorPositions={}, clearBG=False):
    lst = drawInfo.lst

    if clearBG:
        clearRect = (drawInfo.SIDE_BUFFER//2, drawInfo.TOP_BUFFER,
                     drawInfo.window.get_width() - drawInfo.SIDE_BUFFER, drawInfo.height - drawInfo.TOP_BUFFER)
        pygame.draw.rect(drawInfo.window, drawInfo.BACKGROUND_COLOR, clearRect)

    for i, val in enumerate(lst):
        x = drawInfo.startx + i * drawInfo.blockWidth
        y = drawInfo.height - (val - drawInfo.minValue) * drawInfo.blockHeight

        color = drawInfo.GRADIENTS[i % 3]
        if i in colorPositions:
            color = colorPositions[i]

        pygame.draw.rect(drawInfo.window, color, (x, y, drawInfo.blockWidth, drawInfo.height))

    if clearBG:
        pygame.display.update()

def bubbleSort(drawInfo, ascending=True):
    lst = drawInfo.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                drawList(drawInfo, {j: drawInfo.GREEN, j + 1: drawInfo.RED}, True)
                yield True
    return lst

def insertionSort(drawInfo, ascending=True):
    lst = drawInfo.lst
    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascendingSort = i > 0 and lst[i - 1] > current and ascending
            descendingSort = i > 0 and lst[i - 1] < current and not ascending

            if not ascendingSort and not descendingSort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            drawList(drawInfo, {i - 1: drawInfo.GREEN, i: drawInfo.RED}, True)
            yield True

    return lst

def selectionSort(drawInfo, ascending=True):
    lst = drawInfo.lst
    for i in range(len(lst)):
        minIndex = i
        for j in range(i+1, len(lst)):
            if (lst[j] < lst[minIndex] and ascending) or (lst[j] > lst[minIndex] and not ascending):
                minIndex = j
            drawList(drawInfo, {i: drawInfo.GREEN, j: drawInfo.RED}, True)
            yield True

        lst[i], lst[minIndex] = lst[minIndex], lst[i]
        drawList(drawInfo, {i: drawInfo.GREEN, minIndex: drawInfo.RED}, True)
        yield True

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    minVal = 0
    maxVal = 100


    lst = generateStartingList(n, minVal, maxVal)
    drawInfo = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    sortingAlgo = bubbleSort
    sortingAlgoName = "Bubble Sort"
    sortingAlgoGenerator = None

    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sortingAlgoGenerator)
            except StopIteration:
                sorting = False
        else:
            draw(drawInfo, sortingAlgoName, ascending)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generateStartingList(n, minVal, maxVal)
                drawInfo.setList(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sortingAlgoGenerator = sortingAlgo(drawInfo, ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif event.key == pygame.K_i and not sorting:
                sortingAlgo = insertionSort
                sortingAlgoName = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:
                sortingAlgo = bubbleSort
                sortingAlgoName = "Bubble Sort"

            elif event.key == pygame.K_s and not sorting:
                sortingAlgo = selectionSort
                sortingAlgoName = "Selection Sort"

    pygame.quit()

if __name__ == "__main__":
    main()



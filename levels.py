import random
def level1():
    levelParams = [0, 1, 30]
    levelLayout = [(10,50),(20,0),(40,0)]
    return levelLayout
def level2():
    ROWS = 10
    COLUMNS = 8
    BRICKWIDTH = 30
    BRICKHEIGHT = 10
    SPACER = 2
    MARGIN = 5
    layout = []
    brickNum = 1
    for row in xrange(ROWS):
        if row % 2 == 0:
            rowStart = 0
            rowSize = COLUMNS + 1
        else:
            rowStart = BRICKWIDTH / 2
            rowSize = COLUMNS
        y = ( BRICKHEIGHT + SPACER ) * row + MARGIN
        for column in xrange(rowSize):
            brickNum += 1
            x = ( BRICKWIDTH + SPACER ) * column + MARGIN + rowStart
            color = (random.randint(50,255),random.randint(50,255),random.randint(50,255) )
            layout.append( (x, y, BRICKWIDTH, BRICKHEIGHT, color) )
    return layout

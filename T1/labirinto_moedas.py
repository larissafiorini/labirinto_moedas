import random

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
count=0
c=0

def somaCount():
    global count    # Needed to modify global copy of globvar
    count =count+1

def somaCount2():
    global c    # Needed to modify global copy of globvar
    c =c+1

def draw_tile(graph, id, style, width):
    r = "."
    
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"

    if 'start' in style and id == style['start']: r = "A"
    """if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width"""
    if 'muros' in style:
        if id[style['muros'][0]]== style['muros'][1]: r="M"
    if 'paredes' in style:
        if id[style['paredes'][0]] == style['paredes'][1] and r!="S" and c<5:
            r="M"
            somaCount2()
    if 'goal' in style and id == style['goal']: r = "S"
    if 'baus' in style:
        if id[style['baus'][0]]== style['baus'][1] and r!="M" and count<3: 
            r="B"
            somaCount()
    if 'baus' in style and id == style['buracos']: r="[]"
    return r

# ** collects all the keyword arguments in a dictionary
def draw_grid(graph, width=2, **style):

    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)






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
    
    """if 'number' in style and id in style['number']: r = "%d" % style['number'][id]"""
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





import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path


#  Implementação do Algoritmo A* (movimentação até baús e porta de saída):
# A* Algorithm uses a best-first search and finds the least-cost path from a given initial node to one goal node
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
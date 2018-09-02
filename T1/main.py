from labirinto_moedas import *
from A_star import *

diagram = GridWithWeights(10, 10)

#draw_grid(diagram, width=3)
print("\n")
start = (1, 4)

"""O paredão onde a porta de saída está deve ficar sempre nos extremos
da matriz: coluna 9, coluna 0, linha 0 ou linha 9."""
line_list = random.choice([0, 9])
column_line = random.choice([0, 1])

parede_list = random.choice([0, 9])
pared_list = random.choice([0, 9])

# A porta de saída pode ficar em qualquer parte do paredão.
saida = (column_line, line_list)
muros = (column_line, line_list)
baus = (saida[0], abs(saida[1]-1))
paredes = (parede_list, pared_list)
buracos = (random.choice([3, 5,7]), random.choice([3, 5,7]))

came_from, cost_so_far = a_star_search(diagram, start, saida)
print("path até saída do algoritmo A*: ")
print(reconstruct_path(came_from, start, saida))

draw_grid(diagram, width=3, point_to=came_from,start=start, goal=saida, muros=muros, baus=baus, paredes=paredes, buracos=buracos)

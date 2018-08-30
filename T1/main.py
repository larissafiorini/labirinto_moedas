from labirinto_moedas import *
diagram = GridWithWeights(10, 10)

#draw_grid(diagram, width=3)
print("\n")
start, goal = (1, 4), (7, 8)

"""O paredão onde a porta de saída está deve ficar sempre nos extremos
da matriz: coluna 9, coluna 0, linha 0 ou linha 9."""
my_list = random.choice([0, 9])
column_line = random.choice([0, 1])
# A porta de saída pode ficar em qualquer parte do paredão.
saida = (column_line, my_list)
muros = (column_line, my_list)

draw_grid(diagram, width=3, start=start, goal=saida, muros=muros)

my_list = [0, 9]
random.choice(my_list)
#for i in random(0, my_list_len):
#    print(my_list[i])

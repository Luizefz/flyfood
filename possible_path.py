from read_matrix import *
from itertools import permutations

house_pairs = read_matrix('matrix_test.txt') # Devolve um dicionario com as casas(chave) e suas coordenadas(valor)

def generate_paths_possibles(pairs_list=dict):
    permute_list=[]
    key_list = pairs_list.keys()

    for i in key_list:
        if i != 'R':                         # Adiciona na lista todas as chave que nao sao 'R'
            permute_list.append(i)

    permutation = ['R' + ''.join(i) + 'R' for i in permutations(permute_list)] # Gera todas as permutacoes possiveis e adiciona 'R' no inicio e no fim

    return permutation


def generate_pair_distances(pairs_list=dict):   # Gera um dicionario com todas as distancias entre os pares de casas
    conexions_distances = {}
    key_list = pairs_list.keys()       # Pegando a lista de Chaves do dicionário
    
    for i in key_list:                 # Fixa um elemento da lista de chaves e permuta com todos os outros
        for j in key_list:
            if i == j:                 # Ignora a reflexividade da permutacao
                continue
            walk_x = abs(pairs_list[i][0] - pairs_list[j][0])
            walk_y = abs(pairs_list[i][1] - pairs_list[j][1])
            conexions_distances[i+j] = walk_x + walk_y

    return conexions_distances


pair_values = generate_pair_distances(house_pairs)
paths = generate_paths_possibles(house_pairs)

for i in paths:
    for k in range(0, len(i)-1): 
        search = i[k] + i[k+1]                          # Concatena os pares de casas para procurar no dicionario
        print(search, '-',pair_values[search], end=' ') # Imprime o par de casas e a distancia entre elas
    print('\n')

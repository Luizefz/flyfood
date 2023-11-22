from read_matrix import *
from itertools import permutations

def generate_paths_possibles(pairs_list=dict):
    permute_list=[]                          # Gera uma lista com todas as permutacoes possiveis
    key_list = pairs_list.keys()

    for i in key_list:
        if i != 'R':                         # Adiciona na lista todas as chave que nao sao 'R'
            permute_list.append(i)

    permutation = ['R' + ''.join(i) + 'R' for i in permutations(permute_list)] # Gera todas as permutacoes possiveis e adiciona 'R' no inicio e no fim

    return permutation


def generate_pair_distances(pairs_list=dict):
    conexions_distances = {}           # Gera um dicionario com todas as distancias entre os pares de casas
    key_list = pairs_list.keys()       # Pegando a lista de Chaves do dicionário
    
    for i in key_list:                 # Fixa um elemento da lista de chaves e permuta com todos os outros
        for j in key_list:
            if i == j:                 # Ignora a reflexividade da permutacao
                continue
            walk_x = abs(pairs_list[i][0] - pairs_list[j][0])
            walk_y = abs(pairs_list[i][1] - pairs_list[j][1])
            conexions_distances[i+j] = walk_x + walk_y

    return conexions_distances


def calculate_paths_distance(paths=list, pair_values=dict):
    distace = 0                                             # Calcula a distancia de cada caminho
    paths_distances = {}
    for i in paths:
        for k in range(0, len(i)-1): 
            search = i[k] + i[k+1]                          # Concatena em pares de casas para procurar no dicionario
            distace += pair_values[search]                  # Pesquisa no dicionario a distancia correspondente ao par e soma tudo
        paths_distances[i] = distace                        # Adiciona no dicionario de caminhos a chave(caminho) e a soma dos valores(distancia)
        distace = 0
    return paths_distances

matrix_pairs = read_matrix('matrix_test.txt') # Devolve um dicionario com as casas(chave) e suas coordenadas(valor)

paths = generate_paths_possibles(matrix_pairs)
pair_values = generate_pair_distances(matrix_pairs)
paths_distances = calculate_paths_distance(paths, pair_values)

minimal_distance = min(paths_distances, key=paths_distances.get) # Pega a chave com valor de menor distancia
print(f'{minimal_distance} - {paths_distances[minimal_distance]}')
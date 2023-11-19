from read_matrix import *

house_pairs = read_matrix('matrix_test.txt')
house_distances = []

 # Comeca de R e vai permutar em todas as casa possiveis (-R).
# Joga tudo na lista, ordena a lista e pega a menor.
# Proximo caminho n+1 permutando a lista (- R) & (- n+1) [...] 

def generate_path(pairs_list=dict, initial_pair=list):
    conexions_path = []
    final_element = initial_pair[-1]
    key_list = pairs_list.keys()       # Pegando a lista de Chaves do dicionário
    
    for i in key_list:                 # Percorrendo a lista de chaves
        if i == final_element:         # Caso a chave seja igual ao paramentro da chave anterior, pula
            continue                   # Faz a subtracao do Y/X do ultimo elemento com o Y/X do elemento index   
        calc = f'{final_element} - {i}: ({pairs_list[final_element][0] - pairs_list[i][0]}, {pairs_list[final_element][1] - pairs_list[i][1]})'
        
        conexions_path.append(calc)    # Adiciona o passo para cada elemento na lista

    print(conexions_path)

generate_path(house_pairs, ['R','B','D','C']) # Passa a lista completa dos caminhos que já foram visitados
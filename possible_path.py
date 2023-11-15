from read_matrix import *

house_pairs = read_matrix('matrix_test.txt')
house_distances = []

house_now = house_pairs['R'] # Comeca de R e vai permutar em todas as casa possiveis (-R).
                             # Joga tudo na lista, ordena a lista e pega a menor.
                             # Proximo caminho n+1 permutando a lista (- R) & (- n+1) [...] 

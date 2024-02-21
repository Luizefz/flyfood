import os

def read_matrix(file_name):
    file_path = os.path.dirname(os.path.realpath('__file__')) + '\\' + file_name # Cria um file path para pegar a matriz
    matrix_data = []

    with open(file_path, 'r') as f:
        for line in f:
            matrix_data += [[i for i in line.split()]] # Passa linha por linha e guarda os falores em uma matriz.

    matrix_elements = matrix_data[1:][0:]
    matrix_houses = {}

    for y in range(int(matrix_data[0][0])):
        for x in range(int(matrix_data[0][1])):
            if matrix_elements[y][x] != '0':         # Verifica cada elemento, se for != 0, adiciona no dicionario.
                matrix_houses[matrix_elements[y][x]] = (y, x)

    return matrix_houses
                
"""
Use: read_matrix('matrix_test.txt')
"""
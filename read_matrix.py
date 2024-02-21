import os

def read_matrix(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    matrix_houses = {}

    with open(file_path, 'r') as f:
        y = 0
        for line in f:
            if y == 0:
                y += 1
                continue
            
            elements = line.split()
            for x, element in enumerate(elements):
                if element != '0':
                    matrix_houses[element] = (y, x)
            y += 1

    return matrix_houses
                
"""
Use: read_matrix('matrix_test.txt')
"""
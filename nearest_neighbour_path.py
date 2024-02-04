from read_matrix import *
import time


def find_short_path(starter_point: int, remains_point_list: list, matrix_points: dict):
    nearest_distance = float('inf')
    nearest_point = ''

    for point in remains_point_list:
        walk_x = abs(matrix_points[starter_point][0] - matrix_points[point][0])
        walk_y = abs(matrix_points[starter_point][1] - matrix_points[point][1])
        current_distance = walk_x + walk_y

        if current_distance <= nearest_distance:
            nearest_distance = current_distance
            nearest_point = point

    return nearest_point, nearest_distance


def group_shorter_paths(matrix_pairs: dict):
    path = 'R'
    distance = 0
    points = list(matrix_pairs.keys())
    points.remove('R')

    while points != []:
        nearest_point, nearest_distance = find_short_path(path[-1], points, matrix_pairs)
        path += nearest_point
        distance += nearest_distance
        points.remove(path[-1])

        if points == []:
            nearest_point, nearest_distance = find_short_path(path[-1], ['R'], matrix_pairs)
            path += nearest_point
            distance += nearest_distance

    return path, distance


matrix_pairs = read_matrix('matrix_test.txt')

time_start = time.time()
shortest_path, shortest_distance = group_shorter_paths(matrix_pairs)
time_end = time.time()
print(f'{shortest_path} - {shortest_distance}')
print(f'Time: {time_end - time_start}')

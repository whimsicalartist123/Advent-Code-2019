

def get_point_locations(path):
    x, y = 0, 0

    visited_locations = set()
    for instr in path:
        direction = instr[0]
        val = int(instr[1:])

        for _ in range(val):
            if direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'R': x += 1
            else: x -= 1

            visited_locations.add((x, y))

    return visited_locations

def get_intersection_points(path1, path2):
    locations1 = get_point_locations(path1)
    locations2 = get_point_locations(path2)
    return locations1.intersection(locations2)

def manhattan(point):
    return abs(point[0]) + abs(point[1])

with open('data/day3.txt', 'r') as f:
    path1, path2 = [line.strip().split(',') for line in f]


print(min(manhattan(point) for point in get_intersection_points(path1, path2)))


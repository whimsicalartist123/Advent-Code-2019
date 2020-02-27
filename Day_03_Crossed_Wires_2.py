def get_point_locations(path):
    x, y = 0, 0
    num_steps = 0
    visited_locations = {}
    for instr in path:
        direction = instr[0]
        val = int(instr[1:])

        for _ in range(val):
            num_steps += 1
            if direction == 'U': y += 1
            elif direction == 'D': y -= 1
            elif direction == 'R': x += 1
            else: x -= 1

            if (x, y) not in visited_locations:
                visited_locations[(x, y)] = num_steps

    return visited_locations

def get_closest_intersection(path1, path2):
    locations1 = get_point_locations(path1)
    locations2 = get_point_locations(path2)
    intersection = set(locations1).intersection(set(locations2))
    return min(locations1[point] + locations2[point] for point in intersection)

def manhattan(point):
    return abs(point[0]) + abs(point[1])

with open('data/day3.txt', 'r') as f:
    path1, path2 = [line.strip().split(',') for line in f]

print(get_closest_intersection(path1, path2))
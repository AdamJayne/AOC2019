
def trace_wire_grid(path):
    x = 0
    y = 0
    grid = []
    for move in path:
        if move[0] == 'U':
            for step in range(1, int(move[1:]) + 1):
                y += 1
                grid.append((x, y))
        elif move[0] == 'D':
            for step in range(1, int(move[1:]) + 1):
                y -= 1
                grid.append((x, y))
        elif move[0] == 'R':
            for step in range(1, int(move[1:]) + 1):
                x += 1
                grid.append((x, y))
        elif move[0] == 'L':
            for step in range(1, int(move[1:]) + 1):
                x -= 1
                grid.append((x, y))
    return grid
        

with open('./puzzles/day3.txt') as f:

    puzzle = f.read().split('\n')
    wire1 = trace_wire_grid(puzzle[0].split(','))
    wire2 = trace_wire_grid(puzzle[1].split(','))
    intersections = list(set(wire1) & set(wire2))
    distances = map(lambda x: abs(x[0]) + abs(x[1]), intersections)
    print(f'Closest intersection is { min(distances) }')
with open('./puzzles/day2.txt') as f:
    puzzle = list(map(lambda x: int(x), f.read().split(',')))

    puzzle[1] = 12
    puzzle[2] = 2
    
    def process(pos):
        if puzzle[pos] == 1:
            print('Add')
            puzzle[puzzle[pos + 3]] = puzzle[puzzle[pos + 1]] + puzzle[puzzle[pos + 2]]
            return process(pos + 4)
        elif puzzle[pos] == 2:
            print('Multiply')
            puzzle[puzzle[pos + 3]] = puzzle[puzzle[pos + 1]] * puzzle[puzzle[pos + 2]]
            return process(pos + 4)
        elif puzzle[pos] == 99:
            print('END PROGRAM')
            return
    
    process(0)
    print(puzzle)
    print(puzzle[0])
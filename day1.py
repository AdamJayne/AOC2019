
with open('./puzzles/day1.txt', 'r') as f:
    puzzle = f.read().split('\n')
    # Part 1 Solution
    print(sum(map(lambda mass: int(int(mass) / 3) - 2, puzzle[::])))

    # Part 2 Solution
    def calc_fuel(fuel, running=0):
        calculated = int(int(fuel) / 3) - 2
        return calc_fuel(calculated, running+calculated) if calculated > 0 else running
    print(sum(map(calc_fuel, puzzle[::])))
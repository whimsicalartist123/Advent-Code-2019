

def fuel(mass):
    return int(mass/3) - 2

with open("data/masses.txt", "r") as f:
    masses = [int(line) for line in f]
    part1 = sum([fuel(mass) for mass in masses])

print(part1)

def calculate_fuel_for_fuel(mass):
    total = 0
    next_fuel = fuel(mass)

    while next_fuel > 0:
        total += next_fuel
        next_fuel = fuel(next_fuel)
    return total

part2 = sum(calculate_fuel_for_fuel(mass) for mass in masses)
print(part2)
def fuel_required(mass):
    return mass // 3 - 2


def recursive_fuel_required(mass):
    fuel = fuel_required(mass)
    return fuel + recursive_fuel_required(fuel) if fuel > 0 else 0


with open('01.txt') as f:
    modules = list(f)
    print(f'Part 1: {sum(fuel_required(int(mass)) for mass in modules)}')
    print(f'Part 2: {sum(recursive_fuel_required(int(mass)) for mass in modules)}')

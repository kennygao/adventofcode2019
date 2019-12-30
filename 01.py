def fuel_required(mass):
    return mass // 3 - 2


with open('01.txt') as f:
    print(sum(fuel_required(int(mass)) for mass in f))

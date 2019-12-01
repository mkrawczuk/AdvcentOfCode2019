from common import InputForDay

indata = InputForDay(1).get()

print("Part 1: ")
print(sum(map(lambda x: x//3 - 2, indata)))

def countFuel(mass: int):
    if mass < 0:
        return 0
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + countFuel(fuel)

    return countFuel(fuel)

print("Part 2: ")
print(sum(map(countFuel, indata)))

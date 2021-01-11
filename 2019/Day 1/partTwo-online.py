f = lambda mass: mass // 3 - 2

def partial_sum(mass):
    return 0 if f(mass) <= 0 else f(mass) + partial_sum(f(mass))


def part_one():
    with open(r"input.txt") as file:
        return sum(f(int(i)) for i in file.readlines())

def part_two():
    with open(r"input.txt") as file:
        return sum(partial_sum(int(mass)) for mass in file.readlines())

print(part_two())

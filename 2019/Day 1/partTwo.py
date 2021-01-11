f = open('input.txt','r')
d = f.read().split('\n')[:-1]
f.close()

def fuel(input):
	return input // 3 - 2

def calculate_fuel(mass):
	total = 0
	while fuel(mass) > 0:
		mass = fuel(mass)
		total += mass
	return total

total = 0
for i in d:
	total += fuel(int(i))
additional_fuel = calculate_fuel(total)

print("Additional Fuel:", additional_fuel)
print("Mass total:", total)
print("Total:", (total + additional_fuel))

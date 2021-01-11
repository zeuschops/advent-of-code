def f(mass):
	return mass // 3 - 2

def partial_sum(mass):
	to_return = f(mass)
	current = f(mass)
	while f(current) > 0:
		current = f(current)
		to_return += current
	return to_return

def part_one():
	f = open('input.txt','r')
	a = f.read().split('\n')[:-1]
	f.close()
	for i in range(len(a)):
		a[i] = f(int(a[i]))
	return sum(a)

def part_two(a):
	b = []
	for i in range(len(a)):
		b.append(partial_sum(a[i]))
	return sum(b)

f = open('input.txt','r')
a = f.read().split('\n')[:-1]
f.close()

for i in range(len(a)):
	a[i] = int(a[i])

print(part_one())
print(part_two(a))

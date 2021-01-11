f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]
f.close()

x = 0
y = 0
tree_count = 0
#Tree pattern repeats 'many' times, assume modulus is useful
while y != len(d)-1:
	x += 3
	y += 1
	x %= len(d[y])
	if d[y][x] == '#':
		tree_count += 1
print(tree_count)

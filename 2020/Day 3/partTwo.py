f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]
f.close()

#Tree pattern repeats 'many' times, assume modulus is useful
pattern_x = [1,3,5,7,1]
pattern_y = [1,1,1,1,2]
slope_arr = []

def slopes(patt_x,patt_y):
	x = 0
	y = 0
	tree_count = 0
	while y != len(d)-1:
		x += patt_x
		y += patt_y
		x %= len(d[y])
		if d[y][x] == '#':
			tree_count += 1
	return tree_count

for i in range(len(pattern_x)):
	slope_arr.append(slopes(pattern_x[i], pattern_y[i]))
total = slope_arr[0]
for i in range(1,len(slope_arr)):
	total *= slope_arr[i]
print(total)

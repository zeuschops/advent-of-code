f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]
f.close()

print(d)
total = 0
for i in d:
	total += int(int(i) / 3) - 2 #Integer math automatically rounds down every time, yay
print("Total:", total)

f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]
for i in range(len(d)):
	d[i] = int(d[i])
f.close()

for i in range(len(d)):
	for j in range(len(d)):
		for k in range(len(d)):
			if i != j and j != k:
				if d[i] + d[j] + d[k] == 2020:
					print(d[i], d[j], d[k], (d[i]*d[j]*d[k]))

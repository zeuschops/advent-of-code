f = open('input.txt','r')
d = f.read().split('\n')
del d[-1] #Delete the last object since it will always be '' (due to a newline being the ending character with terminal)
f.close()

for i in range(len(d)):
	for j in range(len(d)):
		if i != j:
			if int(d[i]) + int(d[j]) == 2020:
				print('>>>>', d[i], d[j], '\t', int(d[i])*int(d[j]))

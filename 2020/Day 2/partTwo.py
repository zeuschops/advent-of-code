f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]
f.close()

valid_passwds = 0

for i in d:
	n = i.split(' ')
	letter = n[1][0]
	pos_1 = int(n[0].split('-')[0]) - 1
	pos_2 = int(n[0].split('-')[1]) - 1
	if len(n[2]) > pos_1:
		if len(n[2]) >= pos_2:
			if (letter.lower() in n[2][pos_1] or letter in n[2][pos_2].lower()) and n[2][pos_1] != n[2][pos_2]:
				valid_passwds += 1
		else:
			if letter.lower() in n[2][pos_1].lower():
				valid_passwds += 1
print("Valid passwords found:", valid_passwds)

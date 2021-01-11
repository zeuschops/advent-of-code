f = open('input.txt','r')
d = f.read().split('\n')
del d[-1]

correct_count = 0

for i in d:
     data = i.split(' ')
     low = data[0].split('-')[0]
     high = data[0].split('-')[1]
     letter = data[1][0] #Get just 'a' by itself
     count = 0
     for l in data[-1]:
             if letter.lower() in l.lower():
                     count += 1
     if count < int(low) or count > int(high):
             print("INVALID PASSWORD FOUND!", "\n\t" + i)
     else:
             correct_count += 1

print("\nCorrect count:", correct_count)
 

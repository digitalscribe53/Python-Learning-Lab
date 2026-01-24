file = input('Enter file: ')
if len(file) < 1:
   file = 'mbox-short.txt'
handle = open(file)
counts = dict()
lst = list()
for line in handle: 
    if line.startswith('From: '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1 
for key, value in counts.items(): 
    newtup = (value, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

# print(lst)

for value, key in lst: 
   print(key, value)

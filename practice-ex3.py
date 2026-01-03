filename = input('Enter file name: ')
if not filename: 
    filename = 'mbox-short.txt'
handle = open(filename)
counts = dict()
for line in handle: 
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
# --------------------
lst = list()
for key, val in counts.items():
    newtup = (val, key) 
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst:
    print(key, val)
# ---------------------   
# The delineated code could be expressed in 1 line like below:

# print(sorted([(v,k) for k,v in counts.items()]))

# This represents the Python list comprehension syntax, a concise and effecient way to create a new list from existing iterables. 
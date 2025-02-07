## In python sets and hashsets are essentially the same thing, same with dictionaries and Hash maps
## Sets have no duplicates and no indexing like arrays
## Immutable/can not be changed/hashable: Strings, integers, tuples (1,2,3)
## Mutable/not hashable/can be changed: Hashsets,Hashmaps, Arrays/lists"

# Hashsets

s = set()
print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in set - O(1)
if 1 not in s:
  print(True)

# Remove item from set - O(1)
s.remove(3)

print(s)

# Set construction - O(S) - S is the length of the string
string = 'aaaaaaabbbbbbbbbbbccccccccceeeeeeeee'
sett = set(string)

print(sett)

# Loop over items in set - O(n)
for x in s:
  print(x)

# Hashmaps - Dictionaries

## my_dict[num] = i
## in array nums, this sets each num as a key and their value as the index


d = {'greg': 1, 'steve': 2, 'rob': 3}

print(d)

# Add key:val in dictionary: O(1)
d['arsh'] = 4

print(d)

# Check for presence of key in dictionary: O(1)
if 'greg' in d:
  print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
  print(f'key {key}: val {val}')

# TODO: sort this list then do binary search
for i in range(len(V)):
    if V[i] == key:
        hit = i

# BUG: catch the exection for an empty list
mean = sum(V)/len(V)

# The list is often sorted, so we don't user quick sort
V_sorted = heapsort(V)

# If the file exists values are appended, if not a new file is created
store(file_name, V_sorted)

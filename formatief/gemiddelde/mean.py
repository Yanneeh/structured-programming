
# Berekent gemiddelde van een lijst.
def avg(arr):
    return sum(arr)/len(arr)

def arr_avg(arr):
    total = []

    for item in arr:
        total.append(avg(item))

    return avg(total)

# Test succesvol
# print(avg([1, 2]))
# output: 1.5

# Test succesvol
# print(arr_avg([[1,2], [1,2]]))
# output: 1.5

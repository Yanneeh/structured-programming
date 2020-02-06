
# Een functie die twee items in een list verwiseld.
def swap(arr, index_1, index_2):
    el_1 = arr[index_1]
    el_2 = arr[index_2]

    arr[index_1] = el_2
    arr[index_2] = el_1

    return arr

# Test sucessvol.
# arr = swap([2, 3, 4, 6, 7], 0, 1)
# print(arr)
# ouput: [3, 2, 4, 6, 7]


# Een implementatie van het bubble sort algoritme.
def bubble_sort(arr):

    # Stel de gesorteerde index gelijk aan het laatste element van de list.
    sorted_index = len(arr) - 1

    # Check of de lijst al gesorteert is.
    while sorted_index != 0:
        for i in range(len(arr)-1):
            # Check of de waarde van het huidige element
            # groter is dan de waarde van het volgende element.
            if arr[i] > arr[i+1]:
                # Verwissel deze getallen.
                arr = swap(arr, i, i+1)
        sorted_index -= 1
    return arr

# Test succesvol.
# arr = bubble_sort([3, 1, 6, 2, 3])
# print(arr)
# output: [1, 2, 3, 3, 6]

# Test succesvol.
# arr = bubble_sort([4, 3, 8, 1, 9, 6, 2, 5])
# print(arr)
# output: [1, 2, 3, 4, 5, 6, 8, 9]

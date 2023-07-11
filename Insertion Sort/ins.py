def Insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i += 1
    sorted.insert(i, value)

def InsertionSort(input):
    sorted = []
    sorted.append(input[0])
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted

# Example usage:
input_array = [5, 2, 4, 6, 1, 3]
sorted_array = InsertionSort(input_array)
print(sorted_array)


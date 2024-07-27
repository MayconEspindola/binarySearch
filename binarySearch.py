def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

# Exemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for target in range(0, 12):
    result = binary_search(arr, target)
    print(f"The element {target} is at index {result} in the array.")
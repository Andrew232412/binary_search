def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [1, 2, 5, 9.5, 10, 13, 0, 16, 135]


numbers.sort()


target = 13


result = binary_search(numbers, target)
print(f"Искомое число {target} найдено по индексу: {result}" if result != -1 else "Искомое число не найдено.")

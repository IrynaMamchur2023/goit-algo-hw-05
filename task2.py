def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] == x:
            return iterations, arr[mid]

        elif arr[mid] > x:
            right = mid - 1

        else:
            left = mid + 1

    return iterations, arr[left] if left < len(arr) else None


arr = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
x = 2.5
iterations, upper_bound = binary_search(arr, x)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
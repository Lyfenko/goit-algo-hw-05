def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    local_iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        local_iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return local_iterations, arr[mid]

    # Якщо елемент не знайдено, повертаємо "верхню межу"
    if left < len(arr):
        return local_iterations, arr[left]
    else:
        return local_iterations, None


if __name__ == '__main__':
    # Приклад використання:
    sorted_array = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.3, 3.0, 4.5, 5.2]
    target_value = 2.1

    result_iterations, upper_bound = binary_search(sorted_array, target_value)

    if upper_bound is not None:
        print(f"Елемент {target_value} знайдено після {result_iterations} ітерацій. Верхня межа: {upper_bound}")
    else:
        print(f"Елемент {target_value} не знайдено. Верхня межа: {sorted_array[-1]}")

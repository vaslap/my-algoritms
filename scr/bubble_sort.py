# Алгоритм пузырьковой сортировки
# Автор: [Лапунов В.К.]

def bubble_sort(arr):
    """Сортирует список методом пузырька"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
print("До сортировки:", numbers)
sorted_numbers = bubble_sort(numbers.copy())
print("После сортировки:", sorted_numbers)

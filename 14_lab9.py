"""
Задача №1
Напишіть програму, яка реалізує класичний алгоритм тернарного
пошуку заданого елементу у стовпцях двовимірного масиву.
Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.
Автор: Мотовилець Марія 31І
"""
import random

rows, cols = 5, 4
matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

for col in range(cols):
    column = [matrix[row][col] for row in range(rows)]
    column.sort()
    for row in range(rows):
        matrix[row][col] = column[row]

print("Sorted Matrix:")
for row in matrix:
    print(row)

target = int(input("Enter target value: "))
found = False
for col in range(cols):
    low, high = 0, rows - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if matrix[mid1][col] == target:
            print(f"Found {target} in column {col} at row {mid1}")
            found = True
            break
        if matrix[mid2][col] == target:
            print(f"Found {target} in column {col} at row {mid2}")
            found = True
            break
        if target < matrix[mid1][col]:
            high = mid1 - 1
        elif target > matrix[mid2][col]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1
    if found:
        break

if not found:
    print(f"{target} not found in any column")

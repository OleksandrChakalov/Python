def insertion_sort(nums):
    # Сортування починається з 1го елементу (уявляємо що 1ий елемент стоїть на місці)
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Зберігаємо посилання на індекс попереднього елемента
        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляємо елемент
        nums[j + 1] = item_to_insert


list_of_nums = [9, 1, 15, 28, 6, 5005, 2, -78, 98, 3.12, 0]
insertion_sort(list_of_nums)
print(list_of_nums)
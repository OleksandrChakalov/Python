def selection_sort(nums):
    for i in range(len(nums)):

        lowest_value_index = i
        # Цикл перебирає невідсортовані елементи
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Найменший елемент міняємо з першим в списку
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


list= [19, 2999, 0, -67, 0.221, 23230001, 1, -7093, 2]
selection_sort(list)
print(list)

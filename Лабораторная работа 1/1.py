numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)

sum_of_all = sum(num for num  in numbers if num is not None)
count = len(numbers)

average = sum_of_all / (count)

numbers[missing_index] = average

print("Измененный список:", numbers)

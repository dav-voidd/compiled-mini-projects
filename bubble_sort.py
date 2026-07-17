numbers = [150, 4200, 890, 5000, 310]

for i in range(len(numbers)):
    swapped = False
    for j in range(len(numbers) - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
        print(numbers)
        print(swapped)
    if not swapped:
        print("Loop broke early!")
        break
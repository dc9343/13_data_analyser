def calculation_total(numbers):
    total = 0

    for num in numbers:
        total += num
    return total


def calculation_max(numbers):
    max = 0

    for num in numbers:
        if max < num:
            max = num

    return max


def calculation_min(numbers):
    min = numbers[0]

    for num in numbers:
        min < num

    return min


def calculation_ave(numbers):
    ave = calculation_total(numbers) // len(numbers)
    return (ave)

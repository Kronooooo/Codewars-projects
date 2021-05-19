def high_and_low(numbers):
    num = numbers.split(" ")
    for i in range(len(num)):
        num[i] = int(num[i])

    return str(max(num)) + " " + str(min(num))
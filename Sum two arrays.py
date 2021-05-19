def sum_arrays(array1,array2):
    if array1 == [] and array2 == []:
        return []
    num1 = ""
    num2 = ""
    outputArray = []
    for i in array1:
        num1 += str(i)
    
    for i in array2:
        num2 += str(i)
    
    if num1 == "":
        num1 = 0
    if num2 == "":
        num2 = 0

    output = int(num1) + int(num2)
    for i in str(output):
        if i.isdigit():
            outputArray.append(int(i))
        else:
            value = i + str(output[i+1])

    return outputArray

print(sum_arrays([-3,4,2],[3,4,4]))
print(sum_arrays([-1, 2, 2, 5, 3],[6, 7, 8, 5]))
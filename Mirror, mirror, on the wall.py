def mirror(data):
    output = sorted(data)
    start = len(data) - 1
    for i in range(start):
        output.append(output[start-i-1])
    return output
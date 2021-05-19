def number(lines):
    return [str(i+1) + ": " + lines[i] for i in range(len(lines))]

print(number(["a", "b", "c"]))
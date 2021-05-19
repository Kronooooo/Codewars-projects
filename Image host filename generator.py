import random, string

def generateName():
    x = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(6))
    while photoManager.nameExists(x) == True:
        x = generateName()

    return x
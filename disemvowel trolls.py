def disemvowel(string):
    return ''.join([x for x in string if x.lower() not in 'aeiou'])
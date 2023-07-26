def square_digits(num):
    return int(''.join([str(int(x)*int(x)) for x in str(num)]))
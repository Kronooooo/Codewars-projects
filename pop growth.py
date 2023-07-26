def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 *= 1 + percent/100
        p0 += aug
        p0 = p0.__floor__()
        year += 1
    
    return year
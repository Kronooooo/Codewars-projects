def series_sum(n):
    sum = 0
    for i in range(n):
        sum += 1/(1+3*i)
    
    return f"{sum:.2f}"

print(series_sum(1))
print(series_sum(2))
print(series_sum(5))
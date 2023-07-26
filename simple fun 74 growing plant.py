def growing_plant(up_speed, down_speed, desired_height):
    height = 0
    day = 1
    while height + up_speed < desired_height:
        height += up_speed - down_speed
        day += 1
    
    return day

print(growing_plant(100, 10, 910))
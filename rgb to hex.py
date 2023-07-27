def rgb(r: int, g: int, b: int):
    out = ''
    for x in [r, g, b]:
        if x <= 0:
            out += '00'
        
        elif x >= 255:
            out += 'FF'
        
        else:
            out += f'{hex(x)[2:]:>02}'

    return out.upper()
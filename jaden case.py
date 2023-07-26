def to_jaden_case(string: str):
    out = ''
    for word in string.split():
        out += word.capitalize() + ' '
    
    return out.strip()
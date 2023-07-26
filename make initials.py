def abbrev_name(name:str):
    name = name.split()
    return "{}.{}".format(name[0][0], name[1][0]).upper()
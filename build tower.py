def tower_builder(n_floors):
    out = []
    for i in range(n_floors):
        out.append('{star: ^{width}}'.format(star='*'*((2*i)+1), width=(2*n_floors)-1))

    return out

print(tower_builder(1))
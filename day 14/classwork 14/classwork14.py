def no_space(x):
    return x.replace(' ','')
# es funqcia anacvlebs gamotovebul adgilebs carieli adgilit

def count_sheeps(sheep):
    amount_of_sheep = 0
    for element in sheep:
        if element == True:
            amount_of_sheep += 1
    return amount_of_sheep
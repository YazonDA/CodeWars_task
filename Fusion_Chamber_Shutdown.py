# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c,h,o):
    
    water = min(h // 2, o)

    co2 = min(c, (o - water) // 2)

    methane = min(c - co2, (h - water * 2) // 4)

    return water,co2,methane

test = [[(45,11,100),(5,45,0)], [(354,1023230,0),(0,0,354)], [(939,3,694),(1,346,0)]]

for question in test:
    print(f'question == {question[0]}')
    print(f'waiting answer == {question[1]}')
    answer = burner(*question[0])
    print(f'real answer == {answer}\n')
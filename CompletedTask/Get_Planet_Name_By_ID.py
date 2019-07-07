def get_planet_name(id):
    if id == 1: name = "Mercury"
    elif id == 2: name = "Venus"
    elif id == 3: name = "Earth"
    elif id == 4: name = "Mars"
    elif id == 5: name = "Jupiter"
    elif id == 6: name = "Saturn"
    elif id == 7: name = "Uranus"
    elif id == 8: name = "Neptune"
    return name


a = [2, 5, 3, 4, 8, 1]
print(list(map(get_planet_name, a)))


# I`m STUPID!!! One more (((
# +++
# +++
# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)

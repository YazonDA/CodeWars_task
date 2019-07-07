def string_to_array(s):
    return ([i for i in s.split()] if len(s) > 1 else [s])


a = "I love arrays they are my favorite"
print(string_to_array(a))


# I`m STUPID!!!
# +++
# +++
# def string_to_array(string):
#     return string.split(" ")

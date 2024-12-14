# *args = parameter that will pack all arguments into a tuple 
#         useful so that a funcion can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum


print(add(1,10,3))
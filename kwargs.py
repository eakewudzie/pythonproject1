# **kwargs =  parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a carying amoun of keyword arguments

def Hello(**kwargs):
    print("Hello "+ kwargs['first'] + " " + kwargs['last'])



Hello(first="Bro",middle="Dude",last="Code")
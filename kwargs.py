# **kwargs =  parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a carying amoun of keyword arguments

def Hello(**kwargs):
    # print("Hello "+ kwargs['first'] + " " + kwargs['middle'])

    print("Hi", end=" " )
    for key,value in kwargs.items():
        print(value, end=" ")

Hello(title= "Dr" ,first="Eunice",middle="K",last="Ewudzie" )
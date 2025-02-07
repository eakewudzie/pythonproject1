# module = a file containing python code. May contain functions, classes,....etc
# used wih modular programming, which is to separate a program into parts
import myMsg
# import myMsg as m    
# the above is to use to shorten your code
# for instance m.hello and m.bye will perform same task as seen below

# from myMsg import hello,bye -------------can also be used to select specific modules to work with 
# from myMsg import *  will select everything....for instance all (modules) in this module is 
import while_loop
myMsg.hello()
myMsg.bye()

# print("hi")


# help("modules")
help(while_loop)





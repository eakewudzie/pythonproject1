# nested functions calls = function calls inside other function calls
                        #    innermost function calls are resolved first
                        #    returned value is used as argument for the nex outer function



num = input("Enter a whole positive number: ")


num = float(num)
num = abs(num)
num = round(num)
print(num)

# the above can be done using nested func calls


print(round(abs(float(input("Enter any value ")))))

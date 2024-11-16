 #loop Control Statements = Change a loops execution from its normal sequence


 # break = used to terminate the loop entirely
 # continue = skips to he next iteration of the loop
 # pass = does nothing, acts as a placeholder


while True:
    name = input("Enter your name: ")
    if name !="":
        break
#breaks out of the loop when we encounter a value
print("  ")


phone_number = "+495-4444-5555-6"

for i in phone_number:
    if i =="-":
        continue
    print(i, end=" ")


#new line
print("  ")
print("  ")
print("  ")
print("\n")# this also gives a new line

for i in range(1,11):
    if i==3:
        pass
    else:
     print(i, end=" ")

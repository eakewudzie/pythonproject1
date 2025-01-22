# writing a file. After running the program... it creates the file with the name test.txt in our project folder

text = " Hi there\nThis is Eunice. Great to meet you!"
with open('test.txt','w') as file:
    file.write(text)


# to append a text to it, all you have to do is type the statements or texts in the variable text and
#  then replace w with a which stand for append
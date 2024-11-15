  # the inner loop will finish all it's iterations before the outer loop'


rows =int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol: ")


for i in range(rows):
    for m in range(columns):
        print(symbol, end=" ")
    print()
# dictionary = a changeable, unordered collection of unique key:value pairs
                # fast because they use hashing, allow us to access a value quickly


# How Hashing Works in Dictionaries
# Key Conversion: When you add a key to a dictionary, Python computes the hash value of the key using a hashing algorithm.
# Storage: The hash value determines the location in memory where the value associated with the key will be stored.
# Access: When you look up a key, Python recalculates its hash value and retrieves the value directly from the corresponding memory location.


capitals = {"Ghana" : "Accra" ,
            "Germany": "Berlin"}

print(capitals["Germany"])


# The get() method in Python is used with dictionaries to retrieve the value associated with a specified key. It provides a safe way to access dictionary values without raising a KeyError if the key does not exist.

# using the get methid to check the existence of the value of a key
print(capitals.get("Gambia","not available")) # this prints "not available" as specified in the code when the value of the key stated does not exist. otherwise if not stated..the output would be none



# ------------important to note-------------

# Benefits of get()
# Avoids Errors: It prevents the program from crashing when trying to access a non-existent key.
# Provides Default Values: It allows you to return a default value if the key isn't present.





# displaying only keys and values using these methods
print(capitals.keys())
print(capitals.values())

print(capitals.items())#this prints all the items in the dictionary i.e the key and value alike


# anoher way to display all key value pairs is he for loop
for k,v in capitals.items():
    print(k,v)   # where k=key, v=value
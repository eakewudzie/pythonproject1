# dictionary = a changeable, unordered collection of unique key:value pairs
                # fast because they use hashing, allow us to access a value quickly


# How Hashing Works in Dictionaries
# Key Conversion: When you add a key to a dictionary, Python computes the hash value of the key using a hashing algorithm.
# Storage: The hash value determines the location in memory where the value associated with the key will be stored.
# Access: When you look up a key, Python recalculates its hash value and retrieves the value directly from the corresponding memory location.


capitals = {"Ghana" : "Accra" ,
            "Germany": "Berlin"}

print(capitals["Germany"])

print(capitals.get("Gambia","not available"))
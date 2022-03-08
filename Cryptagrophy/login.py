import hashlib
""" Checks the user and password """

user = input("Enter user: ") # Lets user enter own Username
password = input("Enter password: ") # Lets user enter password for user
encoded = password.encode() # Encodes the password
result = hashlib.sha256(encoded).hexdigest() # Creates a SHA256 digest of the plain text password
with open("shadow.txt", "r") as f: # Opens the textfile in READ mode
    stored_user, stored_password = f.read().split(",") # Splits the two values (user, password) 
f.close() # Closes file

if user == stored_user and result == stored_password: # Compare user and password to the once stored in the file
    print("\n")
    print("Logged in Successfully!") # The password ans user is correct
else:
    print("\n")
    print("Login failed!") # No match, either user is wrong, password is wrong or both

print("\n")    
print(stored_password) # Digest of stored password created in registration.py
print(result) # Digest of password from login.py
    




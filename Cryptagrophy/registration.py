import hashlib
""" Create a user and password """

db = open("shadow.txt", "r") # Opens the file shadow.txt in READ-mode
user = input("Please provide your username:") # Let's user enter a personal username
password = input("Choose a password:") # Lets user enter a personal password
encoded = password.encode() # Encodes password (has to be done before hashing)
result = hashlib.sha256(encoded).hexdigest() # Creates a digest through hashing with SHA256
db = open("shadow.txt", "a") # Opens the file in APPEND-mode, this to add info (user and password)
db.write(user + "," + result) # We write the user and password to file, seperated by ","
print("Congratulations!") # After all is done, a congratulation sign can be seen





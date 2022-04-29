import random
# This imports all the punctuation (i.e special characters)
from string import punctuation

# All uppercase password
password = ""
for i in range(10):
    i = chr(random.randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lower case password
password = ""
for i in range(5):
    i = chr(random.randint(65, 90))
    for j in range(5):
        j = chr(random.randint(65,90)).lower()
    password = str(password) + j + i
print(password)

# The upper and lowercase password can be simplified as follows:
password = ""
for i in range(5):
    i = chr(random.randint(65, 90))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)


# Upper, lower case and special characters
# password
# Create a list with all  special characters
special_chars = list(punctuation)  # List with 32 elements in (can determine this by 'print(len(special_chars))')

# Set up the password generator as before
password = ""  # Create an empty string
for a in range(5):  # We want our password to 15 characters (3*5 = 15)
    i = chr(random.randint(65, 90))  # Creates a random upper case character
    j = chr(random.randint(65, 90)).lower()  # Creates a random lower case character
    k = special_chars[random.randint(0, 31)]  # Creates a random special character from our list 'special_chars'
    password = str(password) + i + j + k  # Takes our empty string and adds the random characters we have assigned
    # above. This is repeated 5 times.
print(password)
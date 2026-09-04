# Take password input
password = input("Enter a password : ")

# Check password length
length = len(password)

if length>=8:
        has_good_length = True
else:
    has_good_length = False

# Check for upper case, lower case, numbers and symbols
has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_uppercase = True

    if char.islower():
        has_lowercase = True

    if char.isdigit():
        has_number = True

    if not char.isalnum():
        has_symbol = True

# Calculate password strength score
score = 0

if has_uppercase:
    score = score + 1

if has_lowercase:
    score = score + 1

if has_number:
    score = score + 1

if has_symbol:
    score = score + 1

if has_good_length:
    score = score + 1

# Determine password strength
if score<= 2:
    print(" Password Strength : Weak ")
elif score<=4:
    print(" Password Strength : Medium ")
else:
    print(" Password Strength : Strong ")

# Give suggestion for improvement
if not has_good_length:
    print(" Suggestion : Use atleast 8 characters ")

if not has_uppercase:
    print(" Suggestion : Add an upper case letter ")

if not has_lowercase:
    print(" Suggestion : Add a lower case letter ")

if not has_number:
    print(" Suggestion : Add a number ")

if not has_symbol:
    print(" Suggestion : Add a symbol ")
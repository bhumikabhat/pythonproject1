
#name = input("Enter your full name:")
#phone_number = input("Enter your phone number:")
#result = len(name)
#result = name.find(" ")
#result = name.find("b")
#result = name.rfind("b")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#name = name.find(" ")
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#result = phone_number.replace("-", " ")
#result = phone_number.replace("-",(""))
#print(result)

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username:")

if len(username) > 12:
   print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits" )
else :
    print(f"Welcome {username}")


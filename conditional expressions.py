# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                       Print or assingn one of two values based on a condition
#                        X if condition else Y 

num = 6
a = 6
b = 7
age = 15
temp = 30
user_role = "guest"

print("Negative" if num < 0 else "Positive")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
status = "Major" if age >= 18 else "Minor"
print(status)
weather = "HOT" if temp >= 30 else "COLD"
print(weather)
access_level = "FULL ACCESS" if user_role == "admin" else "LIMITED ACCESS"
print(access_level)
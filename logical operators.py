# logical operators = used on conditional statements

#and =checks if two or more conditions if true
#or =checks if at least one condition is true
#not =true if condition is false,and vise versa

temp =-10
sunny = False

if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

    
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if sunny:
    print ("It's sunny outside")
else :
    print("It's cloudy outside")

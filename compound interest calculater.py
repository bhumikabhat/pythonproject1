# Python compound interest calculater

principle = 0
rate = 0
time = 0

#while principle <= 0:
#    principle = float(input("Enter the principle amount: "))
#    if principle <= 0:
#        print("Principle can't be less than or equal to zero")

#while rate <= 0:
#    rate = float(input("Enter the interest rate amount: "))
#    if rate <= 0:
#        print("interest rate can't be less than or equal to zero")

#while time <= 0:
#   time = int(input("Enter the time in years: "))
#    if time <= 0:
#        print("time can't be less than or equal to zero")

#total = principle * pow((1 + rate / 100), time)
#print(f"Balance after {time} year/s: ${total:.3f}")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("interest rate can't be less than zero")
    else:
        break

while True:
   time = int(input("Enter the time in years: "))
   if time < 0:
        print("time can't be less than zero")
   else:
        break
   
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.3f}")





   
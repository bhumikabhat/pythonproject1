# python weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" :
    weight = weight * 2.205
    print(f"Your weight is {round(weight ,3)} Lbs")
elif unit == "L" :
    weight = weight / 2.205
    print(f"Your weight is {round(weight ,3)} Kgs")
else :
     print(f"{unit} was not valid")


# Temperature Unit Convertor Program
unit= input("What is current unit of measurement (F or C):")
temp= float(input("Enter the temperature: "))

if unit== 'C':
    temp= round((temp* 9/5)+32,1)
    print(f"the temperature in Fahrenheit is: {temp}F ")
elif unit== "F":
    temp= round((temp - 32)*5/9,1)
    print(f"the temperature in Celsius is: {temp}C")
else:
    print("The unit is not valid")
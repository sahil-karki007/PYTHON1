print("Temperature Convertor")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius ")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

a = input("Enter your choice (1-4):")

if a == "1":
    c = float(input("Enter temperature in Celsius:"))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit", f)

elif a == "2":
    f = float(input("Enter temperature in Fahrenheit:"))
    c = (f - 32) * 5/9
    print("temperature in kelvin",c)

elif a == "3":
    c = float(input("Enter temperature in celsius"))
    k = c + 273.15
    print("Temperature in kelvin:",k)

elif a == "4":
    k = float(input("Enter temperature in kelvin:"))
    c = k - 273.15
    print("temperature in celsius:",c)        

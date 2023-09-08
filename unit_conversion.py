def convert_length(meter):
    # if unit=="M":
        feet = meter*3.2
        return feet 
    
# number = int(input("Enter the value in meters: "))
# # unit = input("Enter the unit (M): ").upper()
# result = convert_length(number)
# print("the value in feet is: {} ".format(result))

def convert_temperature(temperature):
    # if unit == "C":
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    
# num = int(input("Enter the celsius temperature: "))
# result = convert_temperature(num)
# print("{} degree celsius is {} degree fahrenheit".format(num,result))

def convert_weight(kilograms):
    # if unit=="kg":
        pounds = kilograms*2.2
        return pounds
# number = int(input("Enter the kilogram value: "))
# result = convert_weight(number)
# print("{} kilograms is {} pounds ".format(number,result))

    
# num_calculations = int(input("How many calculations would you like to perform? "))

# for _ in range(num_calculations):
#     print("Select operation:")
#     print("1. convert length")
#     print("2. convert temperature")
#     print("3. convert weight")
    
    
#     choice = input("Enter choice (1/2/3): ")
    
# if choice in ("1","2","3"):
#     # num = float(input("Enter the degree: "))
#     if choice == '1':
#         num = float(input("Enter the length: "))
#         print("Result:", convert_length(num))
#     elif choice == '2':
#         num = float(input("Enter the temperature: "))
#         print("Result:", convert_temperature(num))
#     elif choice == '3':
#         num = float(input("Enter the weight: "))
#         print("Result:", convert_weight(num))
# else:
#     print("Invalid input")

# print("Calculations completed. Thank you!")






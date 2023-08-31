import math


def calculate_sin(degrees):
    radians = math.radians(degrees)
    # return round(radians,9)
    return(math.sin(radians))

# num= (int(input("enter a degree: ")))
# result = calculate_sin(num)
# print ("the conversion is: {}".format(result))


def calculate_cos(degrees):
    radians = math.radians(degrees)
    # return round(radians,9)
    return round(math.cos(radians),9)

# num= (int(input("enter a degree: ")))
# result = calculate_cos(num)
# print ("the conversion is: {}".format(result))

def calculate_tan(degrees):
    radians = math.radians(degrees)
    # return round(radians,9)
    return round(math.tan(radians),9)

# num= (int(input("enter a degree: ")))
# result = calculate_tan(num)
# print ("the conversion is: {}".format(result))


# num_calculations = int(input("How many calculations would you like to perform? "))

# for _ in range(num_calculations):
#     print("Select operation:")
#     print("1. sin")
#     print("2. cos")
#     print("3. tan")
    
    
#     choice = input("Enter choice (1/2/3): ")
    
# if choice in ("1","2","3"):
#     num = float(input("Enter the degree: "))
#     if choice == '1':
#         print("Result:", calculate_sin(num))
#     elif choice == '2':
#         print("Result:", calculate_cos(num))
#     elif choice == '3':
#         print("Result:", calculate_tan(num))
# else:
#     print("Invalid input")

# print("Calculations completed. Thank you!")

import basic_math
import trig_calculator
import unit_conversion

num_calculations = int(input("How many calculations would you like to perform?: "))

for _ in range(num_calculations):
    print("Select operation:")
    print("1. Basic math operations")
    print("2. Trigonometric calculations")
    print("3. Unit conversions")
    print("4. Exit")
    
    choice = int(input("Enter choice (1/2/3/4): "))
    
    if choice == 4:
        print("Thank you")
        break
    elif choice == 1:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter choice (1/2/3/4/5): "))
        
        if choice in (1, 2, 3, 4):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print("The sum of {} and {} is: ".format(num1,num2), basic_math.add(num1, num2))
        elif choice == 2:
            print("The difference of {} and {} is: ".format(num1,num2), basic_math.subtract(num1, num2))
        elif choice == 3:
            print("The product of {} and {} is: ".format(num1,num2), basic_math.multiply(num1, num2))
        elif choice == 4:
            if num2 == 0:
                print("Division by 0 is undefined")
            else:
                print("The quotient of {} and {} is: ".format(num1,num2), basic_math.divide(num1, num2))

        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid input")
            
    elif choice == 2:
        print("Select operation:")
        print("1. sin")
        print("2. cos")
        print("3. tan")
        print("4. Exit")
        
        choice = int(input("Enter choice (1/2/3/4): "))
        
        if choice in (1, 2, 3):
            num = float(input("Enter the degree: "))
        
        if choice == 1:
            print ("sin {} degree is: {} ".format(num, trig_calculator.calculate_sin(num)))
        elif choice == 2:
            print("cos {} degree is: {} ".format(num, trig_calculator.calculate_cos(num)))
        elif choice == 3:
            print("tan {} degree is: {} ".format(num, trig_calculator.calculate_tan(num)))
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid input")
            
    elif choice == 3:
        print("Select operation:")
        print("1. Convert length")
        print("2. Convert temperature")
        print("3. Convert weight")
        print("4. Exit")
        
        choice = int(input("Enter choice (1/2/3/4): "))
        
        if choice in (1, 2, 3):
            num = float(input("Enter the value to be converted: "))
        
        if choice == 1:
            print("{} meters is {} feet ".format(num, unit_conversion.convert_length(num)))
        elif choice == 2:
            print("{}C is {}F".format(num, unit_conversion.convert_temperature(num)))
        elif choice == 3:
            print("{}kg is {} pound".format(num,unit_conversion.convert_weight(num)))
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("Invalid input")


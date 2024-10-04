def pounds_to_kg(pounds):
    return pounds / 2.20462

def kg_to_pounds(kg):
    return kg * 2.20462

def addition(number_1, number_2):
    sum_result = number_1 + number_2
    return sum_result

def subtraction(number_1, number_2):
    sum_result = number_1 * number_2
    return sum_result

def division(number_1, number_2):
    sum_result = number_1 / number_2
    return sum_result
    
def multiplication(number_1, number_2):
    sum_result = number_1 * number_2
    return sum_result

while True:
    print("Select a function:")
    print("1. Weight Conversion")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Division")
    print("5. Multiplication")

    choice = int(input("Enter the number of the function you want to use: "))

    if choice == 1:
        weight = float(input("Enter your weight: "))
        unit = input("Is this weight in kg or lb? ").lower()

        if unit == "kg":
            print(f"Your weight converted is {kg_to_pounds(weight):.2f} lb")
        elif unit == "lb":
            print(f"Your weight converted is {pounds_to_kg(weight):.2f} kg")
        else:
            print("Invalid unit. Please enter either 'kg' or 'lb'.")

    elif choice == 2:
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        result = addition(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")

    elif choice == 3:
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        result = (num1 - num2)
        print(f"The difference of {num1} and {num2} is: {result}")

    elif choice == 4:
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        result = (num1 / num2)
        print(f"The division of {num1} and {num2} is: {result}")

    elif choice == 5:
        num1 = float(input("Enter your 1st number: "))
        num2 = float(input("Enter your 2nd number: "))
        result = (num1 * num2)
        print(f"The multiplication of {num1} by {num2} is: {result}")
        
    else:
        print("Invalid choice. Please enter a valid function number.")

    continue_choice = input("Do you want to select another option? (yes/no): ")
    if continue_choice.lower() != "yes":
        print("Exiting the program. Thank you!")
        break
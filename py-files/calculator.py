class Calculator:
    
    def addition(self, num1, num2):
        result = num1 + num2
        return result
    
    def subtraction(self, num1, num2):
        result = num1 - num2
        return result
    
    def multiplication(self, num1, num2):
        result = num1 * num2
        return result
    
    def division(self, num1, num2):
        if num2 == 0:
            result = -1
            return result
        else:
            result = num1 / num2
            return result


print("CALCULATOR")


calc = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("\nYour choice (1/2/3/4): ")

if choice == "1":
    result = calc.addition(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = calc.subtraction(num1, num2)
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = calc.multiplication(num1, num2)
    print(f"\nResult: {num1} x {num2} = {result}")

elif choice == "4":
    result = calc.division(num1, num2)
    if result == -1:
        print("Error: Cannot divide by zero!")
    else:
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice! Please enter a number between 1-4.")


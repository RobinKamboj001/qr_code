def calculater():
    print("Simple Calculater")
    print("Optater = + - * /")

    try:
        num1 = float(input("Enter 1st Number = "))
        optater = input("Enter Oprater = +, -, *, / = ")
        num2 = float(input("Enter 2nd Number = "))

        if optater == "+":
            enter = num1 + num2
        elif optater == "-":
            enter = num1 - num2
        elif optater == "*":
            enter = num1 * num2
        elif optater == "/":
            enter = num1 / num2
        else:
             print("Not Found")

        print(f"Total = {enter}")
    except ValueError:
            print("Palese Selact Rignt Number")
calculater()
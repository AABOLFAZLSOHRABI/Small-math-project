while True:
    print("-------------------------")
    print("Please select an option !")
    print("1. math operation")
    print("2. triangle's sides")
    print("3.Exit")
    x = int(input("Enter the number: "))
    print("-------------------------")
    if x == 1:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("error , Please enter number")
        except NameError:
            print("error , Please enter number")
        # A) Arithmetic operations
        Sum = a + b
        diff = a - b
        prod = a * b
        if b != 0:
            div = a / b
            mod = a % b
            int_div = a // b
        else:
            div = "Division by zero is not allowed"
            mod = "Modulus by zero is not allowed"
            int_div = "Integer division by zero is not allowed"
        power_a = a ** 2
        power_b = b ** 2
        print("--------")
        print("Arithmetic operations")
        print("Sum:", Sum)
        print("Difference:", diff)
        print("Product:", prod)
        print("Division:", div)
        print("Modulus:", mod)
        print("Integer Division:", int_div)
        print("Power of a:", power_a)
        print("Power of b:", power_b)


        # C) Binary operations
        print("--------")
        print("Binary operations")
        bin_a = bin(int(a))
        bin_b = bin(int(b))
        addition = bin(int(bin_a, 2) + int(bin_b, 2))
        subtraction = bin(int(bin_a, 2) - int(bin_b, 2))
        multiplication = bin(int(bin_a, 2) * int(bin_b, 2))
        division = bin(int(bin_a, 2) // int(bin_b, 2))
        a_oct = oct(10)
        b_oct = oct(5)
        print("Binary of one = ", bin_a)
        print("Binary of two = ", bin_b)
        print("Binary Addition = ", addition)
        print("Binary Subtraction = ", subtraction)
        print("Binary Multiplication = ", multiplication)
        print("Binary Division = ", division)
        print("a in octal = ", a_oct)
        print("b in octal = ", b_oct)

    elif x == 2:
        print("Enter the sides of the triangle !")
        try:
            S1 = int(input("The first side of the triangle :"))
            S2 = int(input("The second side of the triangle :"))
            S3 = int(input("The third side of the triangle :"))
        except ValueError:
            print("error , Please enter number")
        except NameError:
            print("error , Please enter number")
        if (S1 + S2 > S3) and (S1 + S3 > S2) and (S2 + S3 > S1):
            print("yes")
        else:
            print("no")

    elif x == 3:
        break

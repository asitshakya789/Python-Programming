def add (num1 ,num2):
    return num1 +num2
def subtract (num1 ,num2):
    return num1 - num2
def multiply (num1 ,num2):
    return num1 *num2
def divide (num1 ,num2):
    return num1 /num2
def modulo (num1 ,num2):
    return num1 %num2
print("Please select the operation")
select =int (input("enter the opretion"))
number1 = int(input("Enter first number:-"))
number2 = int(input("Enter seconod number:-"))
if select == 1 :
    print(number1,"+" ,number2,"=", add (number1,number2))
elif select==2:
    print(number1,"-",number2,"=", subtract(number1,number2))
elif select==3:
    print(number1,"*",number2,"=", multiply(number1,number2))
elif select==4:
    print(number1,"/",number2,"=", divide(number1,number2))
elif select==5:
    print(number1,"%",number2,"=", modulo(number1,number2))
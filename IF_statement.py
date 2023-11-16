num1 = input("number1 ?")
num2 = input("number2 ?")
num3 = input("number3 ?")
if num1>num2 and num1>num3:
    if num2>num3:
        print("number " + num1 + " > " + "number " + num2 + " > " + "number " + num3)
    else:
        print("number " + num1 + " > " + "number " + num3 + " > " + "number " + num2)

elif num2>num1 and num2>num3:
    if num1>num3:
        print("number " + num2 + " > " + "number " + num1 + " > " + "number " + num3)
    else:
        print("number " + num2 + " > " + "number " + num3 + " > " + "number " + num1)

else:
    if num1>num2:
        print("number " + num3 + " > " + "number " + num1 + " > " + "number " + num2)
    else:
        print("number " + num3 + " > " + "number " + num2 + " > " + "number " + num1)

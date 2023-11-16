i=0
while i<1:
    num1 = input("first number ?")
    if num1=="exit" or num1=="Exit" or num1=="EXIT":
        i=1
    else:
        op = input("?")
        if op=="exit" or op=="Exit" or op=="EXIT":
            i=1
        else:
            if op=="+" or op=="-" or op=="*" or op=="/":
                num2 = input("second number ?")
                if num2=="exit" or num2=="Exit" or num2=="EXIT":
                    i=1
                else:
                    if op=="+":
                        # num3 = num1 + num2
                        # float(num3)
                        print(str(num1) + " + " + str(num2) + " = " + str(float(num1) + float(num2)))
                    elif op=="-":
                        # num3 = num1 - num2
                        # float(num3)
                        print(str(num1) + " - " + str(num2) + " = " + str(float(num1) - float(num2)))
                    elif op=="*":
                        # num3 = num1 * num2
                        # float(num3)
                        print(str(num1) + " * " + str(num2) + " = " + str(float(num1) * float(num2)))
                    elif op=="/":
                        # num3 = num1 / num2
                        # float(num3)
                        print(str(num1) + " / " + str(num2) + " = " + str(float(num1) / float(num2)))
            else:
                print("error !!! !!! !!!")


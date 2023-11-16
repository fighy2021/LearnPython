time1 = 0
i = 0
n1 = 0

def power(num,time):
    n1 = num
    time += 1
    for time1 in range(time):
        if time1 == 0:            
            print("the " + str(num) + " power " + str(time1) + " is 1")
        else:
            print("the " + str(num) + " power " + str(time1) + " is " + str(n1))
            n1 = n1 * num
            time1 += 1
        




while i<1:
    num1 = input("the num ? ")
    if num1 == "EXIT" or num1 == "Exit" or num1 == "exit" or num1 == "E" or num1 == "e":
        i += 1
    else:
        time1 = input("the power ? ")
        if time1 == "EXIT" or time1 == "Exit" or time1 == "exit" or time1 == "e" or time1 == "E":
            i += 1
        else:                        
            power(int(num1),int(time1))
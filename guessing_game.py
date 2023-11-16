
anser_num = 63
i = 0
a = 0
times = 0
def guess(num1):
    if num1 == anser_num:
        print("Congratulations !! you WIN !!! ")
        return 1
    elif num1 > anser_num:
        print("your number is bigger than anser ")
        return 0
    else:
        print("your number is smaller than anser ")
        return 0



while i<1:
    lim = input("you have to set limit : ")
    while a<1:        
        var1 = input("guess number ! ")
        if var1 == "EXIT" or var1 == "Exit" or var1 == "exit":
            i += 1
        else:
            times += 1            
            a = guess(int(var1))
            if times == int(lim):
                a += 1
                print("you lose")
    print("you try " + str(times) + " times ! ")
    ans = input("try again ? ")
    if ans == "YES" or ans == "Yes" or ans == "yes" or ans == "y" or ans == "Y":
        a = 0
        times = 0
    else:
        i+=1






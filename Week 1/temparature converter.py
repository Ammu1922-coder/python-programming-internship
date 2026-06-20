while(True):
    print("1.Celsius ↔ Fahrenheit")
    print("2.Fahrenheit ↔ Celsius ")
    choice=int(input("Enter choice 1 or 2:"))

    if choice==1:
        celsius=float(input("Enter tempareture in celsius:"))
        fahrenheit=(celsius*9/5)+32
        print("Temparature in Fahrenheit",fahrenheit)

    elif choice==2:
        fahrenheit=float(input("Enter temparature in fahrenheit:"))
        celsius=(fahrenheit-32)*5/9 
        print("Temparature in Celsius",celsius)

    else:
        print("invalid Choice")       

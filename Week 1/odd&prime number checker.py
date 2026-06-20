number=int(input("Enter a Number:"))

if number%2==0:
    print(number,"is a Even number")
else:
    print(number,"is a Odd number")    

#prime number check
if number>=1:
    is_prime=True

    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
        print(number,"is a prime number")
    else:
        print(number,"is not a prime number")

else:
    print(number,"is not a prime number")    
        
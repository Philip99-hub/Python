def prime (number):
    if number > 1:
        for i in range (2,number):
            if number%i == 0:
                print (number, 'is not a prime number')
                print (i, 'times',number//i,'is',number)
                break
        else:
            print (number, 'is a prime number')
    else:
        print (number,'is not a prime number')  

def odd_even(number1):
    if number1%2==0:
        return "even"
    else:
        return "odd"              


# check=odd_even(11)
# print(check)

# number1=int(input("enter the number"))
# print(odd_even(number1))

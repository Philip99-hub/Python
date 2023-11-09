password ="cybersqure"
guess = ""
count=0
while password != guess :
    guess = input("enter the password: ")
    
    count+=1
    
    if password == guess:
        print("login success")
    else :
        print("incorrect password..try again")
    if count==3 :

        break  

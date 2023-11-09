# password="123"
# user_name="abc"

# username=input("enter the user name")
# if username==user_name:
#     input_1=input("enter the password")
#     if input_1==password:
#         print("login succes")
#     else :
#         print("incorrect password..try again")
# else:
#     print("incorrect user name")


# password="123"
# user_name="abc"
# username=input("enter the user name")
# psw=input("enter the password")
# if username==user_name and psw==password :
#     print("login succes")
# else:
#     print("incorrect user name and password try again")

# passwod=[]
# psw=input("enter the password (password should be between 6 to 16 letters):")
# if len(psw)>=6 :
#     if len(psw)<=16:
#         print (psw)
#     else:
#         print("password should not contain more than 16 letters")
# else :
#     print ('password should contain more than 6 letters')


import re
def check_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{6,16}$"
    return re.match(pattern, password) is not None
password = input("Enter a password: ")
if check_password(password):
    print("Valid password.")
else:
    print("Invalid password.")
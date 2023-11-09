def celtofaren(C):
    f=(C * 9/5) + 32
    return f

def farentocel(F):
    c=(F - 32) * 5/9 
    return c

temp=float(input("Enter the temprature you want to convert:"))
unit=str(input("enter the unit(c or f):"))
if unit=="c":
    result_f=celtofaren(temp)
    print("farenheit=",result_f)
elif unit=="f":
    result_c=farentocel(temp)
    print("celsius=",result_c)

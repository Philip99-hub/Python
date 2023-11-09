# fh = open ('testfile.txt','r')
# fh.write('this is my test file for exeption handling')
# fh.close()

# try:
#     fh=open('testfile.txt','w')
#     fh.write('this is my test file for exeption handling')
#     fh.close()
# except FileNotFoundError:
#     print('Error can\'t find file or read the data')
# except IOError:
#     print("read only")
# else:
#     print('Written content in the file successfully')
# finally:
#     print('program execution is finished')

try:
    x=10
    div=int(input("enter a number:"))
    res=x/div
    print(res)
except:
    print("error")
    
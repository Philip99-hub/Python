# for i in range(6):
#     for j in range(i):
#          print ('*',end=' ')
#     print('*')



# for i in range(0,-1):
#     # for j in range(i):
#         print("*",end=" ")
#     # print("*")



for j in range (6):
    for i in range(6):
        print("*")
    print("*",end=" ")




# Define the number of rows
rows = 5

# Loop through each row in reverse order
for i in range(rows, 0, -1):
    # Print asterisks according to the row number
    print("* " * i)

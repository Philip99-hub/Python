price_list=[100,200,4000,300,5000,600]
total=0
for i in price_list :
    print(i)
    total+=i
print ("total",total)

if total > 20000 :
    discount = 25
elif total > 5000:
    discount = 18
elif total >2000 : 
    discount = 12
else :
    discount = 0
netprice=total-total*discount/100
print(netprice)

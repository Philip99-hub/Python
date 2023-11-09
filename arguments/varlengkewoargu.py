def prindetails(item,**kwarguments):
    print('item name is %s'% (item))
    for key,value in kwarguments.items():
        print('- %s is %s'%(key,value))
    return
prindetails("Monitor",price=70,quantity=85)
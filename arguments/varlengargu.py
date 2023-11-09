def prindetails(item,*components):
    print('components of %s are'%(item))
    for component in components:
        print("-",component)
    return
prindetails('computer','cpu','monitor','mothrboard','mouse')
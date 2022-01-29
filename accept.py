open_market = True
f = 1
exe_quantity = int(input()) #from admin
exe_price = int(input())#from admin
if (open_market):
    for i in range(int(input())): #numberofrows in database
        ordertype = input() #fromdatabase
        quantity = int(input())#fromdatabase
        if (exe_quantity > 0):
            if(ordertype.upper() == "LIMIT"):
                price = int(input())#fromdatabase
                if exe_price > price: 
                    f = 0
                else:
                    f = 1
                    exe_quantity = exe_quantity - quantity
            elif(ordertype.upper() == "MARKET"):
                f = 1
            if (f):
                print("ACCEPTED")#goto status
            else:
                print("REJECTED")#goto status

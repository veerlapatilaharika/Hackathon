from datetime import date
def order_date(from_date, to_date):
    day = to_date - from_date
    for i in range(day.days):
        print()#print everything present in database
from_date =  input()#inputfromuser
to_date = input()#inputfromuser
order_date(from_date,to_date)

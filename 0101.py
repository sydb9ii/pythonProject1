import datetime
def return_current_month ():
    date=datetime.datetime.now()
    return date.month

print(return_current_month())
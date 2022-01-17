def calculatePay():
    print("calculating pay")
    inphrs = input("Enter Hours: ")
    hrs = float(inphrs)
    inprate = input("Enter Rate: ")
    rate = float(inprate)
    pay = hrs * rate
    print(pay)
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculatePay()
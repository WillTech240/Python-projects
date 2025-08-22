def seasonm():
    MonthA = input("Enter the current month: ").strip().lower()  
    Autumn = ("september", "october", "november")
    Winter = ("december", "january", "february")
    Spring = ("march", "april", "may")
    Summer = ("june", "july", "august")

    if MonthA in Autumn:
        print("The season is Autumn")
    elif MonthA in Winter:
        print("The season is Winter")
    elif MonthA in Spring:
        print("The season is Spring")
    elif MonthA in Summer:
        print("The season is Summer")
    else:
        print("Invalid month name!")

seasonm()

# self challange makes overtime calcualtor

hours= input("Enter number of hours: ")
h = float(hours)
rate = input("Enter hourly rate: ")
r = float(rate)

pay = (h*r)

if h > 40:
    print("-- Overtime --")
    overrate = r * 0.5
    overtimehours = h - 40
    overpay = (overtimehours * overrate)
    totalpay = overpay + pay
    print("Overtime hours: " + str(overtimehours))
    print("Overtime pay: " + str(overpay))
    print("New total pay: " + str(totalpay))
else: print("No overtime for " + str(h) + " hours.")
    

    

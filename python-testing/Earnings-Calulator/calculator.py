# Default Varialbles used for the calculator selection.

mode = "null"

# Default Variables used for calculating and printing out the results.

earnings_ph = 0         # Used for storing the earnings per hour.
earnings_pd = 0         # Used for storing the earnings per day.
float(earnings_pd)
earnings_pw = 0         # Used for storing the earnings per week.
float(earnings_pw)
earnings_pm = 0         # Used for storing the earnings per month.
float(earnings_pm)
earnings_py = 0         # Used for storing the earnings per year.
float(earnings_py)

hpmt = 1.02

hpd = 0                 # Used for storing how many days you are working per day.
use_hpd = False         # Used to decide if you are using hpd.
hpw = 0                 # Used for storing how many days you are working per day.
use_hpw = False         # Used to decide if you are using hpd.

wdpw = 0                # Used for storing how days you are working per week.
calculate_id = True     # Used to differ between calculating in days and in weeks.


# Select if you are using the calculator to calculate from you monthly salary or your hourly salary.

mode = input("Please choose between the monthly salary calculator and the hourly salary calculator. \r\nTo open the monthly salary calculator press m and enter. \r\nTo open the hourly salary calculator press h and enter. \r\n")

print(chr(27) + "[2J")

if mode == "m":         # Monthly Salary Mode
    earnings_pm = input("Please enter your monthly salary: \r\n")

    wdpw = input("Please enter how many days you are working per week: \r\n")

    calculate_id_raw = input("Please enter If you want to calculate in hours per day or hours per week." + "\r\n" + "If you want to calculate in days type daily and if you want to calculate in weeks type weekly. \r\n")


    # Choose between typing in hours per week or hours per day.

    if calculate_id_raw == "daily":
        calculate_id = True
    elif calculate_id_raw == "weekly":
        calculate_id = False


    # Entering how many hours you are working per day / week.

    if calculate_id == True:
        hpd = input("Please enter how many hours you are working per day: \r\n")
        use_hpd = True
        use_hpw = False
    elif calculate_id == False:
        hpw = input("Please enter how many hours you are working per week: \r\n")
        use_hpw = True
        use_hpd = False

    
    # Changes str and int to float.

    if type(earnings_pm) == str:
        earnings_pm = float(earnings_pm.replace(",","."))
    elif type(earnings_pm) == int:
        earnings_pm = float(earnings_pm) 
    
    if type(earnings_pw) == str:
        earnings_pw = float(earnings_pw.replace(",","."))
    elif type(earnings_pw) == int:
        earnings_pw = float(earnings_pw) 
    
    if type(wdpw) == str:
        wdpw = float(wdpw.replace(",","."))
    elif type(wdpw) == int:
        wdpw = float(wdpw) 

    if type(hpd) == str:
        hpd = float(hpd.replace(",","."))
    elif type(hpd) == int:
        hpd = float(hpd) 

    if type(hpw) == str:
        hpw = float(hpw.replace(",","."))
    elif type(hpw) == int:
        hpw = float(hpw) 


    # Calculates hpd, hpm, hpy.

    hpd = hpw / wdpw

    hpmt = wdpw * hpd
    hpm = hpmt * 4

    hpy = hpm * 12


    # Calculates earnings pw, pd, ph, py.

    earnings_pw = earnings_pm / 30.0
    earnings_pd = earnings_pw / wdpw
    earnings_ph = earnings_pd / hpd
    earnings_py = earnings_pm * 12

    # Prints results.

    print(chr(27) + "[2J")
    print("Days working per week:", wdpw)
    print("Time working per year", hpy)
    print("Time working per month:", hpm)
    print("Time working per week:", hpw)
    print("Time working per day:", hpd)



    print("\r\n")
    print("Earnings per hour:", earnings_ph)
    print("Calculated earnings per day:", earnings_pd)
    print("Calculated earnings per week:", earnings_pw)
    print("Calculated earnings per month:", earnings_pm)
    print("Calculated earnings per year:", earnings_py)



elif mode == "h":       # Hourly Salary Mode
    earnings_ph = float(input("Please enter your earnings per hour: \r\n").replace(",","."))

    wdpw = input("Please enter how many days you are working in a week: \r\n")

    
    calculate_id_raw = input("Please enter If you want to calculate in hours per day or hours per week." + "\r\n" + "If you want to calculate in days type daily and if you want to calculate in weeks type weekly. \r\n")

    if calculate_id_raw == "daily":
        calculate_id = True
    elif calculate_id_raw == "weekly":
        calculate_id = False


    # Entering how many hours you are working per day / week.

    if calculate_id == True:
        hpd = input("Please enter how many hours you are working per day: \r\n")
        use_hpd = True
        use_hpw = False
    elif calculate_id == False:
        hpw = input("Please enter how many hours you are working per week: \r\n")
        use_hpw = True
        use_hpd = False


    if type(hpd) == str:
        hpd = float(hpd.replace(",","."))

    if type(hpw) == str:
        hpw = float(hpw.replace(",","."))

    wdpw = float(wdpw.replace(",","."))

    # Used to calculate earnings per day / week depending on what wasnt given in the step before.

    if use_hpd == True:
        earnings_pd = earnings_ph * hpd
    elif use_hpd == False:
        earnings_pw = earnings_ph * hpw

    if calculate_id == True:
        earnings_pw = earnings_pd * wdpw
    elif calculate_id == False:
        earnings_pd = earnings_pw / wdpw



    earnings_pm = earnings_pd * 30.0
    earnings_py = earnings_pm * 12

    hpmt = wdpw * hpd
    hpm = hpmt * 4

    hpy = hpm * 12

    print(chr(27) + "[2J")
    print("Days working per week:", wdpw)
    print("Time working per year", hpy)
    print("Time working per month:", hpm)
    print("Time working per week:", hpw)
    print("Time working per day:", hpd)



    print("\r\n")
    print("Earnings per hour:", earnings_ph)
    print("Calculated earnings per day:", earnings_pd)
    print("Calculated earnings per week:", earnings_pw)
    print("Calculated earnings per month:", earnings_pm)
    print("Calculated earnings per year:", earnings_py)
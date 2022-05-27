# Default Varialbles used for the calculator selection.

mode = "null"


# Default Variables used for calculating and printing out the results.

earnings_ph = 0         # Used for storing the earnings per hour.
earnings_pd = 0         # Used for storing the earnings per day.
earnings_pw = 0         # Used for storing the earnings per week.
earnings_pm = 0         # Used for storing the earnings per month.
earnings_py = 0         # Used for storing the earnings per year.

hpd = 0                 # Used for storing how many days you are working per day.
use_hpd = False         # Used to decide if you are using hpd.
hpw = 0                 # Used for storing how many days you are working per day.
use_hpw = False         # Used to decide if you are using hpd.

wdpw = 0                # Used for storing how days you are working per week.
calculate_id = True     # Used to differ between calculating in days and in weeks.


# Select if you are using the calculator to calculate from you monthly salary or your hourly salary.

mode = input("Please choose between the monthly salary calculator and the hourly salary calculator. \r\nTo open the monthly salary calculator press m and enter. \r\nTo open the hourly salary calculator press h and enter. \r\n")

if mode == "m":         # Monthly Salary Mode
    print("Not yet done.")

elif mode == "h":       # Hourly Salary Mode
    earnings_ph = input("Please enter your earnings per hour: \r\n")

    wdpw = input("Please enter how many days you are working in a week: \r\n")

    # Choose between typing in hours per week or hours per day.

    calculate_id_raw = input("Please enter If you want to calculate in hours per day or hours per week." + "\r\n" + "If you want to calculate in days type daily and if you want to calculate in weeks type weekly. \r\n")

    if calculate_id_raw == "daily":
        calculate_id = True
    elif calculate_id_raw == "weekly":
        calculate_id = False


    # Entering how many hours you are working per day / week

    if calculate_id == True:
        hpd = input("Please enter how many hours you are working per day: \r\n")
        use_hpd = True
        use_hpw = False
    elif calculate_id == False:
        hpw = input("Please enter how many hours you are working per week: \r\n")
        use_hpw = True
        use_hpd = False


    # Used to calculate earnings per day / week depending on what wasnt given in the step before

    if use_hpd == True:
        earnings_pd = earnings_ph * hpd
    elif use_hpd == False:
        earnings_pw = earnings_ph * hpw

    if calculate_id == True:
        earnings_pw = earnings_pd * wdpw
    elif calculate_id == False:
        earnings_pd = earnings_pw / wdpw

    


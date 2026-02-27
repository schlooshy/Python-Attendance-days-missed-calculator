import time

while True:
    enter = input("Would you like to enter the attendance percentage/days missed calculator? (y/n): ")
    schoolspecific = input("Would you like to use the [schoolname] specific calculator? (y/n): ")
    if enter == "y":
        if schoolspecific == "n":
            print("Count the following from August 1st to July 31st: ")
            holidayweeks = input("Enter the amount of holiday weeks there are: ")
            insetdays = input("Enter the amount of inset days there are: ")
            bankholidays = input("Enter the amount of bank holidays there are: ")
            try:
                holidayweeks = float(holidayweeks)*5
                insetdays = float(insetdays)
                bankholidays = float(bankholidays)
                break
            except ValueError:
                print("Invalid Input!")
                continue

        elif schoolspecific == "y":
            holidayweeks = 39
            insetdays = 5
            bankholidays = 0

        else:
            print("Error!")

        totalbreakdays = holidayweeks + insetdays + bankholidays + 105
        totalschooldays = 365 - totalbreakdays
        onepercent = totalschooldays/100


        while True:
            while True:
                attendance = input("Enter an attendance percentage (no %): ")
                try:
                    attendance = float(attendance)
                    break
                except ValueError:
                    print("Invalid Input, please enter a number! ")
                    continue

            print("Calculating...")
            time.sleep(2.5)

            daysmissed = round(totalschooldays-attendance*onepercent)

            print(f"If you have {attendance}% attendance, you have missed {daysmissed} days of school. ")
            time.sleep(1)

            carryon=input("Would you like to continue? ('n' || exit / any other key || continue) : ")

            if carryon == "n":
                break
            else:
                continue

    elif enter == "n":
        break
    else:
        print("Invalid Input!")
        continue

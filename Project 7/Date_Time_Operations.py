def Date_Time_Task():

    while True:

        print("\n1.Display current date and time")
        print("2.Calculate time difference between two dates")
        print("3.Format date and time in different formats")
        print("4.Stopwatch")
        print("5.Countdown timer")
        print("6.Back to main menu")

        choice = int(input("Choose an option : "))

        match choice:
            case 1:
                from datetime import datetime
                current_datetime = datetime.now()
                print("\nCurrent date and time:", current_datetime)
                    
            case 2:
                from datetime import datetime
                    
                date_format = "%Y-%m-%d"
                date1_str = input("\nEnter the first date (YYYY-MM-DD): ")
                date2_str = input("Enter the second date (YYYY-MM-DD): ")
                    
                try:
                    date1 = datetime.strptime(date1_str, date_format)
                    date2 = datetime.strptime(date2_str, date_format)
                    time_difference = abs(date2 - date1)
                    print("Time difference:", time_difference)
                    
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    
            case 3:
                from datetime import datetime
                    
                date_str = input("\nEnter a date (YYYY-MM-DD): ")
                    
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    print("Formatted date (MM/DD/YYYY):", date.strftime("%m/%d/%Y"))
                    print("Formatted date (DD-MM-YYYY):", date.strftime("%d-%m-%Y"))
                    print("Formatted date (Full Month Name DD, YYYY):", date.strftime("%B %d, %Y"))
                    
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    
            case 4:
                import time
                    
                input("Press Enter to start the stopwatch...")
                start_time = time.time()
                    
                input("Press Enter to stop the stopwatch...")
                end_time = time.time()
                    
                elapsed_time = end_time - start_time
                print("Elapsed time: {:.2f} seconds".format(elapsed_time))
                    
            case 5:
                import time
                    
                countdown_time = int(input("\nEnter countdown time in seconds: "))
                    
                while countdown_time:
                    mins, secs = divmod(countdown_time, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(timeformat, end='\r')
                    time.sleep(1)
                    countdown_time -= 1
                    
                    print("Countdown finished!")
                    
            case 6:
                print("\nReturning to main menu...")
                break
            
if __name__ == "__main__":
    Date_Time_Task()


 
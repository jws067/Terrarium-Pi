import time
run = raw_input("Start? > ")
mins = 0
hrs = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 60 minutes running
    while (True):
        while (mins <= 60):
            print "Minute", mins
            # Sleep for a minute
            time.sleep(60)
            # Increment the minute total
            mins += 1
        hrs += 1
        print "Hours:", hrs
        # Reset the minutes
        mins = 0
        # when hours equals 24 run the pump then reset the hours
        if (hrs == 24):
            hrs = 0
        # Bring up the dialog box here

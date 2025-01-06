'''Hours to minutes'''
def to_minutes(hours,minutes):
    S=int(hours)*60+int(minutes)
    print(f"The conversion of {hours} hours and {minutes} minutes to minutes is:",S)
hours, minutes=input("Enter hours and minutes: ").split()
to_minutes(hours,minutes)

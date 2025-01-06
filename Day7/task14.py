'''Displaying calender of a particular month'''
import calendar

def calender(year,month):
    print(calendar.month(year,month))

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))

calender(year,month)
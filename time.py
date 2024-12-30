import time
#code1
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

#code2
# timestamp = input("Enter current time in HH:MM:SS format: ")
# input_time = time.strptime(timestamp, "%H:%M:%S")
# if(input_time < time.strptime('12:00:00',"%H:%M:%S")):
#   print("Good Morning")
# elif(input_time > time.strptime('12:00:00',"%H:%M:%S") and input_time < time.strptime('18:00:00',"%H:%M:%S")):
#   print("Good Afternoon")
# else:
#   print("Good Evening")

#COde3
hour = int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
  print("Good Morning")
elif(hour>=12 and hour<17):
  print("Good Afternoon")
else:
  print("Good Evening")

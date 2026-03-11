import datetime


century_start = datetime.date(2000,1,1)
today = datetime.date.today()
print(century_start,today)
print("We are",today-century_start,"days into this century")

print("We are",(today-century_start).days,"days into this century")


#datetime.datetime
century_start = datetime.datetime(2000,1,1,0,0,0)
time_now = datetime.datetime.now()
print(century_start,time_now)
print("we are",time_now - century_start,"days, hour, minutes and seconds into this century")


#some_date=datetime.date(2015,2,29)
# some_date =datetime.date(2016,2,29)
some_time=datetime.datetime(2015,2,28,23,59,0)


century_start = datetime.datetime(2000,1,1,0,0,0)
time_now = datetime.datetime.now()
time_since_century_start = time_now - century_start
# print("days since century start",time_since_century_start.days)
# print("seconds since century start",time_since_century_start.total_seconds())
# print("minutes since century start",time_since_century_start.total_seconds()/60)
# print("hours since century start",time_since_century_start.total_seconds()/60/60)



#datetime.time
date_and_time_now = datetime.datetime.now()
time_now = date_and_time_now.time()
print(time_now)


today=datetime.date.today()
five_days_later=today+datetime.timedelta(days=5)
print(five_days_later)

now=datetime.datetime.today()
five_minutes_and_five_seconds_later = now + datetime.timedelta(minutes=5,seconds=5)
print(now)
print(five_minutes_and_five_seconds_later)


now=datetime.datetime.today()
five_minutes_and_five_seconds_earlier = now+datetime.timedelta(minutes=-5,seconds=-5)
print(five_minutes_and_five_seconds_earlier)


time_now=datetime.datetime.now().time() #Returns the time component (drops the day)
print(time_now)

print(time_now+datetime.timedelta(seconds=30))
#Bug or feature?



#But this is Python
#And we can always get around something by writing a new function!
#Let's write a small function to get around this problem
def add_to_time(time_object,time_delta):
    import datetime
    temp_datetime_object = datetime.datetime(2000,1,1,time_object.hour,time_object.minute,time_object.second)
    print(temp_datetime_object)
    return (temp_datetime_object+time_delta).time()


#And test it
time_now=datetime.datetime.now().time()
thirty_seconds=datetime.timedelta(seconds=30)
print(time_now,add_to_time(time_now,thirty_seconds))




#datetime and strings



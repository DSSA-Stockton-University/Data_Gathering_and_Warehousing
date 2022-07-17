# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2022
**Module**: 1
**Week**: 3

---
## Working with Datetimes in Python

![img](/assets/img/2038.png)
---

In python, datetime objects are a way representing various forms of time. Python offers a built-in library called `datetime` for workings with and manipulating various forms of time.

```python
# we import datetime using 
from datetime import datetime
```

__Creating a datetime object__
```python
# to create a datetime object we use the following:
some_date = datetime(year=2021, month=9, day=1)
print(some_date)

# Optionally, there are also arguments for hour, minute, seconds, microseconds and timezone info

# We can also get current time by using:
now = datetime.now()
```

__Formatting Datetimes as strings__
One of the most frequent task you may have to handle is converting a string into a datetime. Thankfully, `datetime.strftime()` does this for us.

```python
date_string = "16 Sep in 2021"
datetime.strftime(date_string, "%d %b in %Y")
```
```
datetime.datetime(2021, 9, 16, 0, 0)
```

Conversely we can turn a datetime into a string
```python
from datetime import datetime

now = datetime.now()

now.strftime("%A, %m, %Y")
```
output
```
'Tuesday, 9, 26, 2021'
```

`strftime()` has a number of formatting styles for working with datetime elements. A cheat sheet is posted below. 

|Code|Example|Description|
|:----|:----|:----|
|%a|Sun|Weekday as locale’s abbreviated name.|
|%A|Sunday|Weekday as locale’s full name.|
|%w|0|Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.|
|%d|08|Day of the month as a zero-padded decimal number.|
|%-d|8|Day of the month as a decimal number. (Platform specific)|
|%b|Sep|Month as locale’s abbreviated name.|
|%B|September|Month as locale’s full name.|
|%m|09|Month as a zero-padded decimal number.|
|%-m|9|Month as a decimal number. (Platform specific)|
|%y|13|Year without century as a zero-padded decimal number.|
|%Y|2013|Year with century as a decimal number.|
|%H|07|Hour (24-hour clock) as a zero-padded decimal number.|
|%-H|7|Hour (24-hour clock) as a decimal number. (Platform specific)|
|%I|07|Hour (12-hour clock) as a zero-padded decimal number.|
|%-I|7|Hour (12-hour clock) as a decimal number. (Platform specific)|
|%p|AM|Locale’s equivalent of either AM or PM.|
|%M|06|Minute as a zero-padded decimal number.|
|%-M|6|Minute as a decimal number. (Platform specific)|
|%S|05|Second as a zero-padded decimal number.|
|%-S|5|Second as a decimal number. (Platform specific)|
|%f|000000|Microsecond as a decimal number, zero-padded on the left.|
|%z|+0000|UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|
|%Z|UTC|Time zone name (empty string if the object is naive).|
|%j|251|Day of the year as a zero-padded decimal number.|
|%-j|251|Day of the year as a decimal number. (Platform specific)|
|%U|36|Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.|
|%W|35|Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.|
|%c|Sun Sep 8 07:06:05 2013|Locale’s appropriate date and time representation.|
|%x|09/08/13|Locale’s appropriate date representation.|
|%X|07:06:05|Locale’s appropriate time representation.|
|%%|%|A literal '%' character.|


__Working date differences__

Often we need to calculate the time multiple datetime objects in python. `datetime` allows us to use simple python operators to accomplish this task

```python
now = datetime.now()
future = datetime(2021,9,29)

diff = now - future
print(diff)
```

__Working with timezones__

Date and time objects may be categorized as aware or naive depending on whether or not they include timezone information.
* aware objects can locate itself relative to other aware objects
* naive object does not contain enough information to unambiguously locate itself relative to other datetime objects. 

The `pytz` module is used for working with time zones. It has two main use cases: 
1. localize timezone-naive datetimes so that they become aware
1. convert a datetime from one timezone to another timezone.

The default timezone for coding is `UTC`. __UTC__ is also called _Coordinated Universal Time_. It is a successor to, but distinct from, Greenwich Mean Time (GMT) and the various definitions of Universal Time. UTC is now the worldwide standard for regulating clocks and time measurement.

All other timezones are defined relative to UTC, and include offsets like UTC+0800 - hours to add or subtract from UTC to derive the local time. 

No daylight saving time occurs in UTC, making it a useful timezone to perform date arithmetic without worrying about the confusion and ambiguities caused by daylight saving time.

```python
import pytz
from pytz import timezone

# Create a datetime object using UTC for the timezone
aware = datetime(tzinfo=pytz.UTC, year=2021, month=1, day=1)

# Create a datetime object with no timezone
unaware = datetime(year=2021, month=1, day=1)

# Create a timezone object for EST
us_tz = timezone("US/Eastern")

# localize the unaware datetime object to EST 
us_aware = us_tz.localize(unaware)

# Time difference between UTC and EST (if we ignore daylights savings)
print(us_aware - aware)
5:00:00

```

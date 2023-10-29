# Additional Constructors

@classmethod
def FromTimeStamp(cls, t):
    "Construct the date from a POSIX timestrap (like time.time())"
    y, m, d, hh, mm, ss, weekday, jday, dst= _time.localtime(t)
    return cls(y, m, d) 

@classmethod
def today(cls):
    "Contruct a date from time.time()"
    t= _time.time()
    return cls.FromTimeStamp(t)

@classmethod
def FromOrdinal(cls, n):
    """ Construct a date from a proleptic Gregorian ordinal.
    January 1 of year 1 is day 1. Only the year, month and day 
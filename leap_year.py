"""
>>> leap_year(1600)
'it is a leap year'
>>> leap_year(1732)
'it is a leap year'
>>> leap_year(1888)
'it is a leap year'
>>> leap_year(1944)
'it is a leap year'
>>> leap_year(2008)
'it is a leap year'


>>> leap_year(1742)
'it is not a leap year'
>>> leap_year(1889)
'it is not a leap year'
>>> leap_year(1951)
'it is not a leap year'
>>> leap_year(2011)
'it is not a leap year'
"""


def leap_year(year):
    """This function returns if a year is leap year or not"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 'it is a leap year'
    return 'it is not a leap year'

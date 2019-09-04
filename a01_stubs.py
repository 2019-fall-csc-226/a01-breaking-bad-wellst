######################################################################
# Author: Taran Wells
# Username: wellst
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
global user_sign
global friend_sign
user_year = int(input("What is your birth year? " ))

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if user_year == 1972 or user_year == 1984 or user_year == 1996 or user_year == 2008:
    user_sign = 1
    print("You are a Rat! \n")
elif user_year == 1973 or user_year == 1985 or user_year == 1997 or user_year == 2009:
    user_sign = 2
    print("You are an Ox! \n")
elif user_year == 1974 or user_year == 1986 or user_year == 1998 or user_year == 2010:
    user_sign = 3
    print("You are a Tiger! \n")
elif user_year == 1975 or user_year == 1987 or user_year == 1999 or user_year == 2011:
    user_sign = 4
    print("You are a Rabbit! \n")
elif user_year == 1976 or user_year == 1988 or user_year == 2000 or user_year == 2012:
    user_sign = 5
    print("You are a Dragon! \n")
elif user_year == 1977 or user_year == 1989 or user_year == 2001 or user_year == 2013:
    user_sign = 6
    print("You are a Snake! \n")
elif user_year == 1978 or user_year == 1990 or user_year == 2002 or user_year == 2014:
    user_sign = 7
    print("You are a Horse! \n")
elif user_year == 1979 or user_year == 1991 or user_year == 2003 or user_year == 2015:
    user_sign = 8
    print("You are a Goat! \n")
elif user_year == 1980 or user_year == 1992 or user_year == 2004 or user_year == 2016:
    user_sign = 9
    print("You are a Monkey! \n")
elif user_year == 1981 or user_year == 1993 or user_year == 2005 or user_year == 2017:
    user_sign = 10
    print("You are a Rooster! \n")
elif user_year == 1982 or user_year == 1994 or user_year == 2006 or user_year == 2018:
    user_sign = 11
    print("You are a Dog! \n")
elif user_year == 1983 or user_year == 1995 or user_year == 2007 or user_year ==2019:
    user_sign = 12
    print("You are a Pig! \n")
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend_year = int(input("What is your friend's birth year?"))
# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
if friend_year == 1972 or friend_year == 1984 or friend_year == 1996 or friend_year == 2008:
    friend_sign = 1
    print("Your friend is a Rat! \n")
elif friend_year == 1973 or friend_year == 1985 or friend_year == 1997 or friend_year == 2009:
    friend_sign = 2
    print("Your friend is an Ox! \n")
elif friend_year == 1974 or friend_year == 1986 or friend_year == 1998 or friend_year == 2010:
    friend_sign = 3
    print("Your friend is a Tiger! \n")
elif friend_year == 1975 or friend_year == 1987 or friend_year == 1999 or friend_year == 2011:
    friend_sign = 4
    print("Your friend is a Rabbit! \n")
elif friend_year == 1976 or friend_year == 1988 or friend_year == 2000 or friend_year == 2012:
    friend_sign = 5
    print("Your friend is is a Dragon! \n")
elif friend_year == 1977 or friend_year == 1989 or friend_year == 2001 or friend_year == 2013:
    friend_sign = 6
    print("Your friend is a Snake! \n")
elif friend_year == 1978 or friend_year == 1990 or friend_year == 2002 or friend_year == 2014:
    friend_sign = 7
    print("Your friend is a Horse! \n")
elif friend_year == 1979 or friend_year == 1991 or friend_year == 2003 or friend_year == 2015:
    friend_sign = 8
    print("Your friend is a Goat! \n")
elif friend_year == 1980 or friend_year == 1992 or friend_year == 2004 or friend_year == 2016:
    friend_sign = 9
    print("Your friend is a Monkey! \n")
elif friend_year == 1981 or friend_year == 1993 or friend_year == 2005 or friend_year == 2017:
    friend_sign = 10
    print("Your friend is a Rooster! \n")
elif friend_year == 1982 or friend_year == 1994 or friend_year == 2006 or friend_year == 2018:
    friend_sign = 1
    print("Your friend is a Dog! \n")
elif friend_year == 1983 or friend_year == 1995 or friend_year == 2007 or friend_year == 2019:
    friend_sign = 12
    print("Your friend is a Pig! \n")
######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year.
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.
if user_sign == 1:
    if friend_sign == 1 or 5 or 9:
        print("You two are a great match!")
    elif friend_sign == 2 or 3 or 4 or 6 or 8 or 10 or 11 or 12:
        print("You two are a match!")
    elif friend_sign == 7:
        print("You two are not a match!")
elif user_sign == 2:
    if friend_sign == 1 or 3 or 4 or 5 or 7 or 9 or 11 or 12:
        print("You two are a match!")
    elif friend_sign == 2 or 6 or 10:
        print("You two are a great match!")
    elif friend_sign == 8:
        print("You two are not a match!")
elif user_sign == 3:
    if friend_sign == 1 or 2 or 4 or 5 or 6 or 8 or 10 or 12:
        print("You two are a match!")
    elif friend_sign == 3 or 7 or 11:
        print("You two are a great match!")
    elif friend_sign == 9:
        print("You two are not a match!")
elif user_sign == 4:
    if friend_sign == 1 or 2 or 3 or 5 or 6 or 7 or 9 or 11:
        print("You two are a match!")
    elif friend_sign == 4 or 8 or 12:
        print("You two are a great match!")
    elif friend_sign == 10:
        print("You two are not a match!")
elif user_sign == 5:
    if friend_sign == 1 or 5 or 9:
        print("You two are a great match!")
    elif friend_sign == 2 or 3 or 4 or 6 or 7 or 8 or 10 or 12:
        print("You two are a match!")
    elif friend_sign == 11:
        print("You two are not a match!")
elif user_sign == 6:
    if friend_sign == 1 or 3 or 4 or 5 or 7 or 8 or 9 or 11:
        print("You two are a match!")
    elif friend_sign == 2 or 6 or 10:
        print("You two are a great match!")
    elif friend_sign == 12:
        print("You two are not a match!")
elif user_sign == 7:
    if friend_sign == 1:
        print("You two are not a match!")
    elif friend_sign == 2 or 4 or 5 or 6 or 8 or 9 or 10 or 12:
        print("You two are a match!")
    elif friend_sign == 3 or 11 or 7:
        print("You two are a great match!")
elif user_sign == 8:
    if friend_sign == 1 or 3 or 5 or 6 or 7 or 9 or 10 or 11:
        print("You two are a match!")
    elif friend_sign == 2:
        print("You two are not a match!")
    elif friend_sign == 4 or 8 or 12:
        print("You two are a great match!")
elif user_sign == 9:
    if friend_sign == 1 or 5 or 9:
        print("You two are a great match!")
    elif friend_sign == 2 or 4 or 6 or 7 or 8 or 10 or 11 or 12:
        print("You two are a match!")
    elif friend_sign == 3:
        print("You two are not a match!")
elif user_sign == 10:
    if friend_sign == 1 or 3 or 5 or 7 or 8 or 9 or 11 or 12:
        print("You two are a match!")
    elif friend_sign == 2 or 6 or 10:
        print("You two are a great match!")
    elif friend_sign == 4:
        print("You two are not a match!")
elif user_sign == 11:
    if friend_sign == 1 or 2 or 4 or 6 or 8 or 9 or 10 or 12:
        print("You two are a match!")
    elif friend_sign == 3 or 7 or 11:
        print("You two are a great match!")
    elif friend_sign == 5:
        print("You two are not a match!")
elif user_sign == 12:
    if friend_sign == 1 or 2 or 3 or 5 or 7 or 9 or 10 or 11:
        print("You two are a match!")
    elif friend_sign == 4 or 8 or 12:
        print("You two are a great match!")
    elif friend_sign == 6:
        print("You two are not a match!")
# TODO print if you are a strong match, no match, or in between

# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  converts the from year, month, day, hour, minute, second to fractional Julian date

# Parameters:
#  year: year
#  month: month
#  day: day
#  hour: hour
#  minute: minute
#  second: second

# Output:
#  Prints the fractional Julian date 
#
# Written by Kristin Eickelbeck
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = float('nan') #year
month = float('nan') #month
day = float('nan') #day
hour = float('nan') #hour
minute = float('nan') #minute
second = float('nan') #second

# parse script arguments
if len(sys.argv)==7:
   year = float(sys.argv[1])
   month = float(sys.argv[2])
   day = float(sys.argv[3])
   hour = float(sys.argv[4])
   minute = float(sys.argv[5])
   second = float(sys.argv[6])
else:
   print(\
    'Usage: '\
    'python3 ymdhms_to_jd.py year month day hour minute second'\
   )
   exit()

# write script below this line

JD = day - 32075 + 1461*(year+4800+ (month-14)/12)/4 + 367*(month - 2 - (month-14)/12 *12)/12 -3*((year+4900+(month-14)/12)/100)/4
JD_midnight = JD - 0.5
D_fractional = (second + 60 *(minute+60*hour))/86400
jd_frac = (JD_midnight + D_fractional)//1

print(jd_frac)



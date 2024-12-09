# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  This script calculates the maximum achievable bitrate

# Parameters:
#  tx_w: Transmitter power (W)
#  tx_gain_db: Transmitter gain (dB)
#  freq_hz: Frequency of transmission (Hz)
#  dist_km: Distance between transmitter and receiver (km)
#  rx_gain_db: Receiver gain (dB)
#  n0_j: Noise spectral density (J)
#  bw_hz: Bandwidth (Hz)

# Output:
#  The script will print the maximum achievable bitrate
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
c =  2.99792458e8 #speed of light

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
tx_w = float('nan') #Transmitter power (W)
tx_gain_db = float('nan') #Transmitter gain (dB)
freq_hz = float('nan') #Frequency of transmission (Hz)
dist_km = float('nan') #Distance between transmitter and receiver (km)
rx_gain_db = float('nan') #Receiver gain (dB)
n0_j = float('nan') #Noise spectral density (J)
bw_hz = float('nan') #Bandwidth (Hz)

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line
Ll = 10**(-1/10) #Line loss
La = 10**(0/10) #atmospheric loss
lam = c/freq_hz; #wavelength
S = dist_km * 10**3 #distance in meters

C = tx_w*Ll*tx_gain_db*(lam/(4*math.pi*S))**2*La*rx_gain_db
N = n0_j*bw_hz

r_max = bw_hz*math.log((1+C/N),2)

print(math.floor(r_max))



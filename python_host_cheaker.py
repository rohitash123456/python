import os # Importing main libs
import sys
start = "" # Setting up variables
range1 = 0
range2 = 0
for carg in sys.argv: # Checking for arguments
    if carg == "-s":
        argnum = sys.argv.index(carg)
        argnum += 1
        start = sys.argv[argnum]
    elif carg == "-r1":
        argnum = sys.argv.index(carg)
        argnum += 1
        range1r = sys.argv[argnum]
        range1 = int(range1r)
    elif carg == "-r2":
        argnum = sys.argv.index(carg)
        argnum += 1
        range2r = sys.argv[argnum]
        range2 = int(range2r)
print ("[*] Host Scanner launched!") # Informs user about initialize
if start == "": # Checks if all the information is provided
    print ("[E] No host provided")
elif range1 == 0:
    print ("[E] No range1 provided")
elif range2 == 0:
    print ("[E] No range2 provided")
else:
    if range1 > range2:
        count = range1 - range2
    elif range1 < range2:
        count = range2 - range1
    for ccount in range(range1, range2): # Counts the IP range to ping
            target = start + "." + str(ccount)
            response = os.system("ping " + target + " 2>&1 >/dev/null") # Sets response to ping
            if response == 0: # Reads response, checks if it is 0
                err = 0 # sets err to 0
            else:
                err = 1 # sets err to 1
            if err == 0: # when err is equal to 0
                print ("[+] " + target + " is up!") # Informs user about hosts that are up

import subprocess
import datetime
import random
import os
ic = input("Pick an option (cancel by inputting any non-options):\n1) Backup only apps/data to file\n2) Full Device Backup\n3) Restore backup\n")
o = ["1","2","3"]
currentdir = "backups/"
dto = str(datetime.date.today())
rng = random.randrange(1,255)
fileprefix = currentdir + dto + "-" + str(rng) + "-"
chk = subprocess.check_output("adb devices", shell=True)
chkrs = ''.join(filter(str.isalnum, chk.decode("utf-8")))
if chkrs == "Listofdevicesattached":
    print("Error: No device attached.")
    exit()
if ic not in o:
    print("Canceled!")
    exit()
else:
    lsapps = subprocess.check_output("adb shell pm list packages -3", shell=True)
    dcd = lsapps.decode("utf-8")
    spllines = dcd.splitlines()
    applist = [x[8:] for x in spllines]
    if ic == "1":
        print("Printing app list:")
        for x in applist: print(x)
        ic2 = input("\nDo you wish to back up each application with its data? \n")
        if ic2.lower() != "y":print("Canceled!"); exit()
        else:
            strlist = str(applist)
            applistline = ''
            for x in strlist:
                if x != '[' and x != ']' and x != ',' and x != "'":
                    applistline += x
            try:
                r = os.system("adb backup -apk -f " + fileprefix + "user-app-backup" + ".ab" + " " + applistline)
                print(r)
            except:
                print("error")
    if ic == "2":
        print("Printing app list:")
        for x in applist: print(x)
        icv = input("\nDo you wish to back up your entire device to file? \n")
        if icv.lower() != "y":print("Canceled!"); exit()
        else:
            try:
                r = os.system("adb backup -apk -shared -all -f " + fileprefix + "fullbackup.ab")
            except:
                print("error")
    if ic == "3":
        print("printing list of backup folders:")
        lsdirs = os.listdir(currentdir)
        print(*lsdirs, sep="\n")
        ic3 = input("Please type a file to restore from. (Case Sensitive) \n")
        if ic3 not in lsdirs:
            print("Invalid Input... Exiting...")
            exit()
        if ic3 in lsdirs:
            print("restoring...")
            try:
                r = os.system("adb restore " + currentdir + ic3)
            except:
                    print("An error occured while installing " + ic3)

import subprocess
import datetime
import random
import os
ic = input("Pick an option (cancel by inputting any non-options):\n1) Backup all apps\n2) Reinstall from backup\n")
o = ["1","2"]
currentdir = "backups"
dto = str(datetime.date.today())
rng = random.randrange(1,255)
workingdir = currentdir + "/backup-" + dto + "-" + str(rng) + "/"
chk = subprocess.check_output("adb devices", shell=True)
chkrs = ''.join(filter(str.isalnum, chk.decode("utf-8")))
if chkrs == "Listofdevicesattached":
    print("Error: No device attached.")
    exit()
if ic not in o:
    print("Canceled!")
    exit()
else:
    if ic == "1":
        print("Good To Go")
        lsapps = subprocess.check_output("adb shell pm list packages -3", shell=True)
        dcd = lsapps.decode("utf-8")
        spllines = dcd.splitlines()
        applist = [x[8:] for x in spllines]
        print("Printing app list:")
        for x in applist: print(x)
        ic2 = input("\nDo you wish to back up each application? \n")
        if ic2.lower() != "y":print("Canceled!"); exit()
        else:
            os.mkdir(workingdir)
            for pkg in applist:
                findapp = subprocess.check_output("adb shell pm path " + pkg, shell=True)
                apploc = findapp.decode("utf-8")
                cfn = apploc[-9:]
                clfn = apploc[8:]
                if cfn[0:8] == "base.apk":
                    print("Extracting " + pkg)
                    try:
                        r = os.system("adb pull " + clfn.rstrip('\n') + " " + workingdir + pkg + ".apk")
                        print(r)
                    except:
                        print("error")
                else:
                    print("error")
                    print(cfn)
                    print(len(cfn))

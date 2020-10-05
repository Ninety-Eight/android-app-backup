# android-app-backup
Backup and Restore Apps on Your Android, using ADB

# Getting Started
You need the following:

-ADB\
-Command-line application\
-Linux PC. Untested on Win/Mac.\
-Whatever USB cable your phone uses\
-A phone that actually turns on and operates\
-Python 3+

How to use ADB: https://www.xda-developers.com/install-adb-windows-macos-linux/


# What does this do and how does it work?

This application will pull all installed applications from your Android user profile, and place them into a folder in the /backups/ directory. You can then restore from this folder backup at a later point.

# I meet the requirements. What do I do?

Simply use the command-line application of your choice to navigate to the folder of this repository, and run the python file.

# Does this work on Windows?

I actually don't know since I don't use Windows. It should work if ADB is in the path but otherwise I have no clue. If it works/doesn't on Windows, please let me know and I will update this.

# More info

This is a very simple script that isn't designed to have all the features in the world. If you want to contribute to it, you can do so with a pull request. If you want to modify it, you can do whatever you want to it.

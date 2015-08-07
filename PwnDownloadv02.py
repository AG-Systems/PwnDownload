import urllib
import time
testfile = urllib.URLopener()

yes = set(['yes','y', 'ye', ''])

no = set(['no','n'])

print (" Welcome to PwnDownload v0.2. Made and programmed by AurigaX ")

time.sleep(1)
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])

print (" Do you want to install a web browser? ")


guess = int(input("1 = Yes, and 2 = No" )

if guess == 1
    print (" Which one do you want to install ")
    brow = int(input("1 = chrome, and 2 = Firefox" )
    if brow == 1
        testfile.retrieve("http://www.google.com/chrome/", "ChromeSetup.exe")
    else:
        print (" Firefox is for scrubs. Please use the botnet")
        
if guess == 0

#testfile.retrieve("https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe", "SteamSetup.exe")
#
#testfile.retrieve("https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409", "vs_community.exe")
#testfile.retrieve("download.deluge-torrent.org/windows/deluge-1.3.11-win32-setup.exe", "deluge-1.3.11-win32-setup.exe")

print ("Finished running the program")

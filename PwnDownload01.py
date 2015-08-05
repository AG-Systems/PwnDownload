import urllib
testfile = urllib.URLopener()
print (" Welcome to PwnDownload v0.1. Made and programmed by AurigaX ")
testfile.retrieve("https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe", "SteamSetup.exe")
testfile.retrieve("http://www.google.com/chrome/", "ChromeSetup.exe")
testfile.retrieve("https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409", "vs_community.exe")
testfile.retrieve("download.deluge-torrent.org/windows/deluge-1.3.11-win32-setup.exe", "deluge-1.3.11-win32-setup.exe")

print ("Finished running the program")

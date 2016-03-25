from unzipfiles import unzipfile
import sys
import os
from os.path import basename
import glob

print("Enter the input file name: ")
inputfilename = input()

# Here creating a new directory with the zip file name with the assumption that it will be mostly unique
# Then creating a sub-directory with the same name. This will be renamed to the ServerName since we don't have it yet

filenameonly = basename(inputfilename)
filenameonly = filenameonly[:filenameonly.find(".cab")]

rootdirectory = "C:/Pradeep/data/extract/" + filenameonly

if not os.path.exists(rootdirectory):
    os.makedirs(rootdirectory+ "/" + filenameonly)

unzipfile(inputfilename, rootdirectory+ "/" + filenameonly)

# Now navigating to that directory and picking "ServerName_System_Information.txt"
# Then extracting the ServerName from it and renaming the directory

SysInfoFile = glob.glob(rootdirectory + "/" + filenameonly + "/*System_Information.txt")

# Using basename to get only the file name. Since this returns a list using [0]
# then looking for the first occurence of "_" and got the list in return
# again fetching the 0th element

FirstServerName = basename(SysInfoFile[0]).split("_",1)[0]

# Now renaming the folder using newly got ServerName

os.rename(rootdirectory+ "/" + filenameonly, rootdirectory+ "/" + FirstServerName)

# Here finding the server names based on the *cluster.log files
servernames =[]

for clusterlog in glob.glob(rootdirectory + "/" + FirstServerName + "/*_cluster.log"):
    servernames.append(basename(clusterlog).split(("."),1)[0])

# Got the server names. Now checking if the corresponding folders exist
# If don't exist create it, prompt the user for the cab file


for servername in servernames:
    if os.path.exists(rootdirectory +"/" + servername.upper()):
        print("Folder " + servername + " exists. Not doing anything here")
    else:
        os.makedirs(rootdirectory+ "/" + servername.upper())
        print("Enter the path of the new zip file for server: " + servername.upper())
        inputfilename = input()
        unzipfile(inputfilename, rootdirectory + "/" + servername.upper())

print("All files extracted")
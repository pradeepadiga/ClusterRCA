import os
import sys
import glob
import re

def GetHotFix(rootdirectory, servernames,outputfile):
    FinalList = []
    for servername in servernames:
        outputfile.write("~" * 20 + "\n" + "Filter Drivers loaded on " + servername + "\n" + "~" * 20 + "\n" * 2)
        hotfixfile = glob.glob(rootdirectory + "/" + servername.upper() + "/*_Hotfixes.TXT")[0]



        KBListNames = "kb"+servername.upper()
#        KBListNames.append(KBListName)
        KBListName = []

        with open(hotfixfile, "r", encoding="utf-8") as Hotfix:
            for line in Hotfix:
                #columns = line.split("  ")
                #KBListName.append(columns[4:5])
            #print(KBListName[3:])
                column = str(line.split(' '))
                m = str(re.findall(r'\bKB.*\b', column))
                string = m.split(',')
                KBArticles = re.sub('["\'\[\]]', '', string[0])
                KBListName.append(KBArticles)
            KBListName[0]=servername
            FinalList.append(KBListName)
#            print(KBListName)
#            print(FinalList[:100])

    #Comparing the dynamically created lists
    i=0
    while i<len(FinalList):
        print("Hotfixes missing on Server: " + FinalList[i][0])
        print(set(FinalList[i][1:]) - set(FinalList[i - 1][1:]))
        i=i+1

    #
    #

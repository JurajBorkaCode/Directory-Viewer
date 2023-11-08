import sys
import os

args = sys.argv

loc = args[1]


def list_files(loc,indent):
    for file in os.listdir(loc):
        if "." in file:
            print("  "*indent+"|"+file)
        else:
            print("  "*indent+"|"+file)
            try:
                list_files(loc+'\\'+file,indent+1)
            except:
                pass



list_files(loc,0)
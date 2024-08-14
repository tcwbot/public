###
# removes everything, but the in-between text using delimiter strings
# Script helps log analysis issue isolation, When logs are of 10-100 Gigabytes large.
# written : tcwbot
###
import sys, re

# Error condition
if len(sys.argv)<=2:
    print("Usage: (help)\n\t$ python delimit.py \'delimitingString\' exactFilename")
    exit()  # early exit

# Finds all indices that match delimiter, only use first and last indices 
# to remove unwanted data and keeping the in between.
def parsefile(): 
    try:
        f = open(sys.argv[2], "r")
        content_list = f.read().splitlines()
        arr=[]
        j=0
        for i in content_list:
            #if i==sys.argv[1]:
            if bool(re.search(sys.argv[1],i)):
                arr.append(j)
            j+=1
        j=0
        while(j<len(content_list)):
            if not (j in range(arr[0],arr[-1]+1)):
                print(content_list[j])
            j+=1
    except IOError: 
            print("No such file or directory:",sys.argv[2])
    finally:
        f.close()

if __name__=='__main__':
    parsefile()

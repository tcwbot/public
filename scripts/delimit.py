# delimites and removes everything in between.. only

import sys

# Error condition
if len(sys.argv)<=1:
    print("`Usage: (help)\n\t$ python delimit.py \'delimitingString\' exactFilename")
    exit()  # early exit

def parsefile(): 
    try:
        f = open(sys.argv[2], "r")
        content = f.read()
        content_list = content.splitlines()
        f.close()
        arr=[]
        j=0
        for i in content_list:
            if i==sys.argv[1]:
                arr.append(j)
            j+=1

        j=0
        while(j<len(content_list)):
            if not (j in range(arr[0],arr[-1]+1)):
                print(content_list[j])
            j+=1
    except IOError: 
            print("No such file or directory:",sys.argv[2])

parsefile()

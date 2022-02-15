# Gets All Certificate of Achievement at CCSF
import requests
from bs4 import BeautifulSoup
import time
import threading
from threading import Thread

global FILENAME
global STOP
FILENAME="certs.txt"
STOP=1558
#STOP=15

def check_file():
    # if file exists overwrite.
    f = open(FILENAME, "w")
    f.close

def remove_all(list,elem):
    while elem in list:
        list.remove(elem)

def get_all_certs(group):
    for i in group:
        f = open(FILENAME, "a")
        #print(str(int(i/STOP * 100)),"% progess",end='\r')
        uri="https://ccsf.curricunet.com/Report/Program/GetReport/" + str(i) + "?reportId=29"
        try:
            page = requests.get(uri, timeout=2)
            soup = BeautifulSoup(page.text, 'html.parser')
            title = soup.findAll('div',attrs={"class":"Title"})
            try:
                title=title[0].text
                title=list(title)
                remove_all(title,"\n")
                remove_all(title,"\t")
                remove_all(title,"\r")
                f.writelines(f'{i:4} {"".join(title)}\n')
            except:
                pass
        except: 
            pass
        finally:
            f.close()

def run(group):
    print('hi',group)

def main():
    check_file()
    #all=get_all_certs()

    max_per_thread=25
    exit=True
    arr = list(range(2000))
    print(len(arr)/4)
    arr.reverse()
    i=0
    while(exit):
        out=[]
        try:
            for x in range(max_per_thread):
                out.append(arr.pop())
        except IndexError:
            exit=False
        group=out
        try:
            i+=1
            #print(str(int(i/len(arr))),"% progess",end='\r')
            print(i,end='\r')
        except:
            pass
        th=Thread(target=lambda: get_all_certs(group))
        th.start()
    th.join()
if __name__=="__main__":
    main()
else:
    exit()

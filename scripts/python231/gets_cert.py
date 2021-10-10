231cs-python $ cat gets_cert.py 
# Gets All Certificate of Achievement at CCSF
# Adds all list to file certs.txt
import requests
from bs4 import BeautifulSoup

def remove_all(list,elem):
    while elem in list:
        list.remove(elem)

def get_all_certs():
    #for i in range(1,1558):
    stop=1558
    certs=[]
    for i in range(1,stop):
        print(str(int(i/stop * 100)),"% progess",end='\r')
        uri="https://ccsf.curricunet.com/Report/Program/GetReport/" + str(i) + "?reportId=29"
        try:
            page = requests.get(uri)
            soup = BeautifulSoup(page.text, 'html.parser')
            title = soup.findAll('div',attrs={"class":"Title"})
            try:
                title=title[0].text
                title=list(title)
                remove_all(title,"\n")
                remove_all(title,"\t")
                remove_all(title,"\r")
                certs.append("".join(title))
            except:
                pass
        except:
            pass
    return certs

all=get_all_certs()
with open('certs.txt', 'a') as f:
    f.writelines("%s\n" % i for i in all)
    f.close()

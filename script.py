#!/usr/bin/python3

#Libraries
import requests
import bs4
from datetime import datetime
import sys
import time
import csv
import os.path

#Timer
start = time.time()

#Proxy Tor
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

#Directory
pathDirectory = os.path.dirname(os.path.realpath(__file__))

#CSV Header
headerMaster = ['Domain', 'Title', 'Statut', 'Date']

#Creation of the csv file
csvMasterFile = open('result_master.csv', 'w', encoding='UTF8')
writerMaster = csv.writer(csvMasterFile)
writerMaster.writerow(headerMaster)

#Create an empty list
myList = []

#Main functions
def extractTitle():
     title = html.title.text
     print("Title : "+title)
     myList.append(title.replace(',','-'))

def statut():
     if response.status_code == 200:
          print("Statut : " + "ONLINE")
          myList.append("ONLINE")
     else:
          print("Status_code : " + str(response.status_code))
          myList.append(str(response.status_code))

def date():
     todayDate = datetime.now()
     dt_string = todayDate.strftime("%d/%m/%Y %H:%M:%S")
     print("Date :", dt_string)
     myList.append(dt_string)

#Start
print("===== STARTING SEARCH =====")
counter = 0

with open(pathDirectory+'/'+sys.argv[1]) as list:
     for domain in list:
          domain = domain.strip('\n')
          counter = counter + 1
          print("   ")
          print("** Analysis of the domain n°" + str(counter) + " **")
          print("Domain : "+ domain)
          myList.append(domain)
          try:
               response = session.get(domain)
               html = bs4.BeautifulSoup(response.text, "html.parser")
               extractTitle()
               statut()
               date()
               print(">> Adding a new line in the csv file <<")
               print(myList)
               writerMaster.writerow(myList)
               title = html.title.text
               myList = []
               time.sleep(1)
          except requests.exceptions.ConnectionError:
               print("Statut : " + "OFFLINE")
               myList.append('N.A')
               myList.append('OFFLINE')
               date()
               writerMaster.writerow(myList)
               print(">> Adding a new line in the csv file <<")
               print(myList)
               myList = []
               time.sleep(1)
               pass
          except Exception as exc:
               print("Statut : " + "UNKNOWN")
               myList.append('N.A')
               myList.append('UNKNOWN')
               date()
               writerMaster.writerow(myList)
               print(">> Adding a new line in the csv file <<")
               print(myList)
               myList = []
               print("<!> Catching an error :" + str(exc) + " <!>")
               time.sleep(1)
               pass


#CSV number of lines
print("   ")
print("Number of line in the csv result file: " + str(counter))

#Time
elapsedTime = time.time() - start
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsedTime)))
print("   ")

#End
print("===== ENDING SEARCH =====")

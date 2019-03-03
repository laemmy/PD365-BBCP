#!/usr/bin/env python3
# 
import requests
import json


URL="https://repeatermap.de/api.php"
result=requests.get(URL)
repeater=result.json()

def print_csv():

  #print ('999;',i,';','a;',format(call,tx),tx,str(rx-tx),mode)
 # print (call,qth,rx,tx,str(rx-tx),mode)

    print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format("999",i,"a",channelname,"",frequency,shift,"","","","","","","","",lat,lon,"","","","","","","","H","","","None"))


i=0

print("0;num;type;callsign;dmrid;qrg;shift;cc;mix;ctcss;net;city;cnty;country;ctry;lat;lon;longcall;callext1;callext2;txcontact1;rxgroup1;txcontact2;rxgroup2;pwr;scanlist1;scanlist2;scanlistfm")

for r in repeater["relais"]:
    
    # Nicht alle Repeater haben lat und lon
    # Hier sollte dann ueber Locator gefiltert
    # werden
    lat = r["lat"] if "lat" in r else 0
    lon = r["lon"] if "lon" in r else 0

    loc = r["locator"]
    mode = r["mode"]

    rx = r["rx"]
    tx = r["tx"]

    frequency = str(tx).replace(".",",")
    shift = float(round(rx-tx,1))
    
    call  = r["call"]
    qth = r["qth"]
    channelname = call + " " + str(r["tx"])


    if mode != "FM":
        continue

    if tx < 430 or tx > 440:
        continue

    if loc[:4] in ["JO61","JO62","JO63"]: 
        i = i +1
        print_csv()

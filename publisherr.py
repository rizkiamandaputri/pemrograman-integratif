#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
import requests
import json

print("Jalankan pub")
name = input('Masukkan Nama Artist : ')
url="https://api.deezer.com/search?q=%s&appid=c660e7387bmsh89d212a4e0753dep10ef84jsn24c7347a23d6"
data = requests.get(url % (name)).json()

# untuk mempublish
def on_publish(client, userdata, mid):    
    print("mid: "+str(mid))

client = mqtt.Client()
client.on_publish = on_publish

client.username_pw_set("username","password")
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

print("Publisher mempublish ke topik")
    # print(judul)

# perulangan untuk mengirimkan data (publish) ke mqtt broker setiap detik
while True:
    for i in data['data']:
        title = str(i['title'])
        title_short = str(i['title_short'])
        title_version = str(i['title_version'])
        duration = str(i['duration'])
        rank = str(i['rank'])
        client.publish("title :",title, qos=1)
        client.publish("title_short :",title_short, qos=1)
        client.publish("title_version :",title_version, qos=1)
        client.publish("duration :",duration, qos=1)
        client.publish("rank :",rank, qos=1)
        time.sleep(5)
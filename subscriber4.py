import paho.mqtt.client as mqtt

# fungsi yang dipanggil pertama untuk melakukan subscribe ke mqtt broker
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber 4 connected with result code: "+str(mid)+" "+str(granted_qos))

# fungsi yang bertujuan untuk menampilkan data yang berhasil diterima subscriber
def on_message(client, userdata, msg):
    print("Subscriber 4 receive : "+msg.topic+" "+str(msg.payload))

client4 = mqtt.Client()
client4.on_subscribe = on_subscribe
client4.on_message = on_message

# client.username_pw_set("username","password")
client4.connect("broker.hivemq.com", 1883, 60)
client4.subscribe([("duration :",1)],qos=1)
client4.loop_forever()
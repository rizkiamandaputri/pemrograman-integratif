import paho.mqtt.client as mqtt

# fungsi yang dipanggil pertama untuk melakukan subscribe ke mqtt broker
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber 1 connected with result code : "+str(mid)+" "+str(granted_qos))

# fungsi yang bertujuan untuk menampilkan data yang berhasil diterima subscriber
def on_message(client, userdata, msg):
    print("Subscriber 1 receive : "+msg.topic+" "+str(msg.payload))

client1 = mqtt.Client()
client1.on_subscribe = on_subscribe
client1.on_message = on_message

# client.username_pw_set("username","password")
client1.connect("broker.hivemq.com", 1883, 60)
client1.subscribe([("title :",1)],qos=1)
client1.loop_forever()
import paho.mqtt.client as mqtt

# fungsi yang dipanggil pertama untuk melakukan subscribe ke mqtt broker
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber 2 connected with result code: "+str(mid)+" "+str(granted_qos))

# fungsi yang bertujuan untuk menampilkan data yang berhasil diterima subscriber
def on_message(client, userdata, msg):
    print("Subscriber 2 receive : "+msg.topic+" "+str(msg.payload))

client2 = mqtt.Client()
client2.on_subscribe = on_subscribe
client2.on_message = on_message

# client.username_pw_set("username","password")
client2.connect("broker.hivemq.com", 1883, 60)
client2.subscribe([("title_short :",1)],qos=1)
client2.loop_forever()
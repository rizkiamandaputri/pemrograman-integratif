import paho.mqtt.client as mqtt

# fungsi yang dipanggil pertama untuk melakukan subscribe ke mqtt broker
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber 3 connected with result code: "+str(mid)+" "+str(granted_qos))

# fungsi yang bertujuan untuk menampilkan data yang berhasil diterima subscriber
def on_message(client, userdata, msg):
    print("Subscriber 3 receive : "+msg.topic+" "+str(msg.payload))

client3 = mqtt.Client()
client3.on_subscribe = on_subscribe
client3.on_message = on_message

# client.username_pw_set("username","password")
client3.connect("broker.hivemq.com", 1883, 60)
client3.subscribe([("title_version :",1)],qos=1)
client3.loop_forever()
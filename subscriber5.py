import paho.mqtt.client as mqtt

# fungsi yang dipanggil pertama untuk melakukan subscribe ke mqtt broker
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscriber 5 connected with result code: "+str(mid)+" "+str(granted_qos))

# fungsi yang bertujuan untuk menampilkan data yang berhasil diterima subscriber
def on_message(client, userdata, msg):
    print("Subscriber 5 receive : "+msg.topic+" "+str(msg.payload))

client5 = mqtt.Client()
client5.on_subscribe = on_subscribe
client5.on_message = on_message

# client.username_pw_set("username","password")
client5.connect("broker.hivemq.com", 1883, 60)
client5.subscribe([("rank :",1)],qos=1)
client5.loop_forever()
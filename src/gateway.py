import json
from random import randint
import time

import paho.mqtt.client as mqtt

BROKER = "demo.thingsboard.io"
PORT = 1883
ACCESS_TOKEN = "sswSGdprouSo5Py7cKon"
TELEMETRY_TOPIC = "v1/devices/me/telemetry"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TELEMETRY_TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic + ":" + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(ACCESS_TOKEN)
client.connect(BROKER, PORT)

client.loop_start()
while 1:
    temperature = randint(0, 60)
    light = randint(0, 100)
    print(temperature, light)
    client.publish(TELEMETRY_TOPIC, json.dumps({
        'temperature': temperature,
        'light': light,
    }))
    time.sleep(5)

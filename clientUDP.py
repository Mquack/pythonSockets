import socket
from w1thermsensor import W1ThermSensor
from datetime import datetime
from time import sleep

SERVER = "192.168.1.169"
PORT = 5055

sensor = W1ThermSensor()

var = "HELLO!!!"

def getTemps():
    temps = []

    for sensor in W1ThermSensor.get_available_sensors():
        temps.append(sensor.get_temperature())

    firstSensor = str(round(temps[0]-2, 1))
    secondSensor = str(round(temps[1]-2, 1))
    currentDate = datetime.now().strftime('%Y-%m-%d %H:%M')
    packet = (firstSensor + " " + secondSensor + " " + currentDate)
    return packet


while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            packet = getTemps()
        except:
            print("no data")
            packet = "nodata"
        client.sendto(packet.encode("utf-8"),(SERVER,PORT))
    except:
        print("Cannot connect...")
    sleep(5)

#client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#client.sendto(var.encode("utf-8"),(SERVER,PORT))

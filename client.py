import socket
from w1thermsensor import W1ThermSensor
from datetime import datetime
from time import sleep

SERVER = "192.168.1.169"
PORT = 5055
HEADER = 32
ENDMSG = "%DISC%"


sensor = W1ThermSensor()


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
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER, PORT))
        try:
            pkt = getTemps()
        except:
            print("no data")
            pkt = "nodata"
        packet = pkt.encode("utf-8")
        msgLength = str(len(packet)).encode("utf-8")
        msgLength += b' ' * (HEADER - len(msgLength))

        client.send(msgLength)
        client.send(packet)

        endConnection = ENDMSG.encode("utf-8")
        msgLength = str(len(endConnection)).encode("utf-8")
        msgLength += b' ' * (HEADER - len(msgLength))
        client.send(msgLength)
        client.send(endConnection)
    except:
        print("Cannot connect...")

    sleep(5)

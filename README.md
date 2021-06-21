# pythonSockets
Simple script to send some data, in this case from a Raspberry Pi but easily changable to another purpose, from one machine to another.

There are 2 version, one using SOCK_STREAM(TCP) and another using SOCK_DGRAM(UDP).
UDP is simpler and quicker, but less reliable.
TCP is a bit slower but makes sure the data actually is received.

In both versions one(client) machine sends temperature data from an Dallas DS18B20 sensor to a second(server) machine that saves that data in a regular text file with a newline added.
There are two sensors connected to the Pi, one for outside and one for inside. These two, together with the date and time is send as a packet to the server.

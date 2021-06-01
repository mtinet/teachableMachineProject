import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
    if "Arduino" in p.description:
        print("This is an Arduino!")

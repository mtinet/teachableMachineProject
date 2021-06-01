import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())

# # 마이크로비트 연결 com 포트 찾아서 연결하기
# for port, desc, hwid in sorted(ports):
#     if 'USB' in desc:
#         com = port
# if com != '':
#     print('\n microbit USB detected: ', com)
# else:
#     print('\nPlease connect your microbit to this PC via USB')
#
# ser = serial.Serial(com, 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=0)


# # 시리얼통신으로 연결된 포트리스트를 보여주고 아두이노 포트 찾기
# print("연결되어 있는 시리얼 포트 리스트는 다음과 같습니다.\n")
# for p in ports:
#     print(p)
#     if "Arduino" in p.description:
#         print("This is an Arduino!")

# 아두이노 연결 com 포트 찾아서 연결하기
for port, desc, hwid in sorted(ports):
    if 'Arduino' in desc:
        com = port
if com != '':
    print('\n arduino USB detected: ', com)
else:
    print('\nPlease connect your microbit to this PC via USB')

ser = serial.Serial(com, 9600, timeout=0)

import serial.tools.list_ports

# 연결된 포트 리스트 확인하기
ports = list(serial.tools.list_ports.comports())


# # 마이크로비트 연결 com 포트 찾아서 연결하기
# 연결된 포트 보여주기
# for p in ports:
#     print(p)

# 마이크로비트 포트번호 보여주기
# for port, desc, hwid in sorted(ports):
#     if 'USB' in desc:
#         com = port
# if com != '':
#     print('\n microbit USB detected: ', com)
# else:
#     print('\nPlease connect your microbit to this PC via USB')
#
# 마이크로비트가 연결된 시리얼 포트를 마이크로비트의 시리얼 통신 기본속도인 115200보레이트로 연결하기
# ser = serial.Serial(com, 115200, timeout=0, parity=serial.PARITY_NONE, rtscts=0)


# # 시리얼통신으로 연결된 포트리스트를 보여주고 아두이노 포트 찾기
# 연결된 포트 보여주기
# print("연결되어 있는 시리얼 포트 리스트는 다음과 같습니다.\n")
# for p in ports:
#     print(p)
#     # 아두이노 포트번호 보여주기
#     if "Arduino" in p.description:
#         print("This is an Arduino!")

# 아두이노 연결 com 포트 찾아서 연결하기
# 연결된 포트 보여주고 내림차순 한 리스트에 Arduino라는 문자가 있으면 포트를 com 변수에 넣기
for port, desc, hwid in sorted(ports):
    if 'Arduino' in desc:
        com = port
# com변수가 비어있지 않으면 아두이노 포트를 보여주기
if com != '':
    print('\n arduino USB detected: ', com)
else:
    print('\nPlease connect your microbit to this PC via USB')

# 아두이노과 연결된 시리얼 포트를 아두이노의 시리얼 통신 기본속도인 9600보레이트로 연결하기
ser = serial.Serial(com, 9600, timeout=0)

# teachableMachineProject

## python_local_converted_keras  

### 파이썬에 tensorflow, PIL(pillow), numpy, cv2, serial 라이브러리를 설치해 사용함  

#### 0. 관련 링크  
- [관련 영상](https://photos.app.goo.gl/G8MU8mmxGLo6pj2D9)  
- [Teachable Machine](https://teachablemachine.withgoogle.com/)  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/example.png?raw=true)  

#### 1. 개요  
- 로컬에서 웹캠 영상을 가져와서 학습된 모델에 있는 레이블의 정규화된 비율로 데이터를 출력함  
- 정규화된 특정 결과값의 비중에 따라 시리얼 통신으로 utf-8의 형태의 'a', 'b', 'c'를 송신함  
- 송신된 데이터에 의해 동작하는 간단한 Arduino 파일을 첨부함  
- 아두이노 파일(dataReceiveTest.ino)은 'a'가 들어오면 13번핀을, 'b'가 들어오면 12번핀을, 'c'가 들어오면 11번핀을 제어하도록 프로그래밍되어 있음  
- 아두이노 파일(robot_hands_three servo.ino)은 3개의 서보모터를 사용하여 'a'가 들어오면 rock을, 'b'가 들어오면 paper를, 'c'가 들어오면 scissors를 내도록 프로그래밍되어 있음  
- 아두이노 파일(dataReceiveTest.ino)은 2개의 서보모터를 사용하여 'a'가 들어오면 paper를, 'b'가 들어오면 scissors를, 'c'가 들어오면 rock을 내도록 프로그래밍되어 있음  

#### 2. python 설치  
- tensorflow는 아직 python 3.7까지만 지원을 하므로, 파이썬을 3.7버전으로 설치해야 함  
- python.org사이트 Diwbkiad-Windows에서 Python 3.7.7 - March 10, 2020 카테고리 안에 있는 Download Windows x86-64 executable installer를 다운로드 받아 설치함, [링크](https://www.python.org/downloads/windows/)  
- python 설치할 때는 Add python 3.7 to PATH를 반드시 체크하고 설치를 진행하세요  
![](https://miro.medium.com/max/1308/1*2b0JT1QLGfkzYIoofh9VEA.png)  

#### 3. 라이브러리 설치  
- tensorflow 설치(최근에 tensorflow가 2.0으로 버전 업그레이드가 되면서 그냥 pip install tensorflow 를 할 경우 자동으로 2.0버전이 설치되고, 우리가 사용하고 있는 파이썬에서 라이브러리 구동이 안됨. 따라서 이전 버전을 강제로 설치해야함)  
```{.python} 
pip install tensorflow==1.15
```

- 텐서플로우 msvcp140.dll오류시 참고 사이트 [링크](https://blog.naver.com/complusblog/221177145686), [마이크로소프트사 설치링크](https://www.microsoft.com/ko-kr/download/details.aspx?id=48145)  

##### 추가 오류 1  
```
Fatal error in launcher: Unable to create process using '"c:\python39\python.exe"  "C:\Python39\Scripts\pip.exe" install tensorflow': ??? ??? ?? ? ????.
```
- tensorflow를 설치할 때 Fatal 오류가 나는 경우는 자동으로 구동되는 환경변수의 path 설정에 오류가 있기 때문이다. pip를 다시 설치하는 아래 조치를 통해 해결할 수 있다. 
```
where python
```
위 명령어를 통해 python을 실행파일 위치를 파악하고 환경변수를 수정하면 해결이 가능하나, 이후 실행하는 pip 명령어를 아래와 같은 형태로 수정하여 실행하면 일단은 실행 가능함

```
pip install *********

대신에 

python -m pip install **********

의 형태를 사용함
```

- PIL을 설치  
```{.python} 
pip install pillow 
```
- serial을 설치
```{.python} 
pip install pyserial
```
- cv2 설치
OpenCV의 main module만 사용한다면 아래처럼 설치
```{.python} 
pip install opencv-python
```
만약 main module과 extra module을 같이 사용하고 싶다면 아래처럼 설치합니다.
```{.python} 
pip install opencv-contrib-python  
```
- 그 외 오류는 오류나는 부분을 카피해서 구글에 물어보면 해답을 얻을 수 있음  


##### 추가 오류 2  
```
  File "C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\tensorflow_core\python\keras\saving\hdf5_format.py", line 160, in load_model_from_hdf5
    model_config = json.loads(model_config.decode('utf-8'))
AttributeError: 'str' object has no attribute 'decode'
```
- 해당위치의 파일로 들어가서 아래와 같이 표기된 부분을 모두 삭제하거나, 
```
.decode('utf-8')
```

- 아래 명령어를 실시해 자동으로 삭제해줌  
```
pip3 install "h5py<3.0.0" --user
```

##### 추가 오류 3  
```
Traceback (most recent call last):
  File "teachableMachineByVideo.py", line 42, in <module>
    model = tensorflow.keras.models.load_model('keras_model.h5', compile=False)
......
    raise ValueError('Unknown ' + printable_module_name + ': ' + class_name)
ValueError: Unknown layer: Functional
```
- teachable machine이 신규 업데이트 되면서 모델을 변형할 때 사용하는 keras도 버전이 업데이트 되었으나, 기존에 tensorflow==1.15에 함께 설치되는 keras 버전은 2.3.1이기 때문에 생기는 오류  

- 아래 명령어를 통해 keras를 2.4.0으로 업데이트 해주면 잘 동작함  
```
python -m pip install keras==2.4.0  
```

##### 추가 오류 4  
```
0 Class 1 : 0.715531
b'a\n'
Traceback (most recent call last):
  File "teachableMachineByVideo.py", line 128, in <module>
    if prediction[:, 2] > 0.7 :
IndexError: index 2 is out of bounds for axis 1 with size 2
```

- 현재 teachableMachineByVideo.py 파일은 3개의 레이블 이상이 있을 때 제대로 동작하게 짜여져 있는데, 2개의 레이블만 있는 모델 파일을 사용할 때 발생하는 오류  

- 3번 째 레이블을 사용하게 하는 부분인 해당 파일의 128~131번째 줄을 아래와 같이 해당 행의 앞쪽에 '#'을 추가해서 주석처리하여 동작하지 않도록 해주면 됨  
```
    # if prediction[:, 2] > 0.7 :
    #    send = (str('c')+'\n').encode("utf-8")
    #    ser.write(send)
    #    print(send)
```        


 
#### 4. 파일 구동은 아래 명령어로 하면 됨, 프로그램 정지는 'q'버튼  
```{.python}  
$python teachableMachineByVideo.py  
```  

#### 5. 결과 이미지  
주의사항 : 가위바위보와 결과 속의 얼굴은 서로 무관하고, 학습시킬 때 나눈 클래스의 총 합계 퍼센트가 늘 100%가 나오는 것임, 어떤 화면이 입력되건 총 합계는 100%라는 말. 학습을 잘 시키는 것도 중요하고, 디폴트값을 넣어주는 것도 중요하다는 사실을 알 수 있음  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/scissors.png?raw=true)  


#### 6. 그 외 파일들의 기능은 다음과 같다.  
- keras_model.h5 : teachable machine 홈페이지에서 Export한 모델파일, 이 파일이 머신러닝 학습의 결과이며, 이 파일을 이용해 학습된 내용을 활용함, 현재는 파란색, 흰색, 초록색을 구분하는 모델파일이 올라가 있음. 티처블 머신으로 자신이 학습시키고자 하는 이미지를 학습시키면 됨  
- labels.txt : 모델을 만들 때 레이블을 몇개로 해 학습을 시켰느냐에 따라 label이 나뉨, label 이름을 자신이 원하는 것으로 수정해 학습시키면 추후 모델로 추론을 할 때 그 label이 표시됨, 물론 나중에 다운로드 받은 labels.txt 파일을 직접 수정해도 무관함  
- teachableMachineByVideo.py : 학습된 모델 파일로 웹캠에서 입력되는 영상을 분석하여 추론해주는 파이썬 파일, 이 파일이 이 프로젝트의 핵심, 추후 라즈베리파이에 탑재해서 로봇을 제어하는데 사용할 예정  
- arduino/dataReceive.ino : 학습된 데이터를 기반으로 추론한 결과가 특정 퍼센티지를 넘을 때 바이트 형태의 데이터를 전송하는데, 그 때 아두이노에서 데이터가 잘 받아지는지를 확인하는 코드, 'a'가 바이트의 형태로 잘 넘어오면 13번 핀(또는 칩LED)가 점멸함, 'b'는 12번, 'c'는 11번 핀을 점멸함  
- arduino/robot_hands.ino : 'a'가 넘어오면 바위, 'b'가 넘어오면 보자기, 'c'가 넘어오면 가위를 내는 로봇팔 제어 프로그램  

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
- 아두이노 파일은 'a'가 들어오면 13번핀을, 'b'가 들어오면 12번핀을, 'c'가 들어오면 11번핀을 제어하도록 프로그래밍되어 있음  

#### 2. python 설치  
- tensorflow는 아직 python 3.7까지만 지원을 하므로, 파이썬을 3.7버전으로 설치해야 함  

#### 3. 라이브러리 설치  
- tensorflow 설치(최근에 tensorflow가 2.0으로 버전 업그레이드가 되면서 그냥 pip install tensorflow 를 할 경우 자동으로 2.0버전이 설치되고, 우리가 사용하고 있는 파이썬에서 라이브러리 구동이 안됨. 따라서 이전 버전을 강제로 설치해야함)  
```{.python} 
pip install tensorflow==1.15
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
 
 
#### 4. 파일 구동은 아래 명령어로 하면 됨, 프로그램 정지는 'q'버튼  
```{.python}  
$python teachableMachineByVideo.py  
```  

#### 5. 그 외 파일들의 기능은 다음과 같다.  
- keras_model.h5 : teachable machine 홈페이지에서 Export한 모델파일, 이 파일이 머신러닝 학습의 결과이며, 이 파일을 이용해 학습된 내용을 활용함, 현재는 파란색, 흰색, 초록색을 구분하는 모델파일이 올라가 있음  
- labels.txt : 모델을 만들 때 레이블을 몇개로 해 학습을 시켰느냐에 따라 label이 나뉨  
- teachableMachineByVideo.py : 학습된 모델 파일로 웹캠에서 입력되는 영상을 분석하여 추론해주는 파일, 이 파일이 이 프로젝트의 핵심, 추후 라즈베리파이에 탑재해서 로봇을 제어하는데 사용할 예정  
- arduino/dataReceive.ino : 학습된 데이터를 기반으로 추론한 결과가 특정 퍼센티지를 넘을 때 바이트 형태의 데이터를 전송하는데, 그 때 아두이노에서 데이터가 잘 받아지는지를 확인하는 코드, 'a'가 바이트의 형태로 잘 넘어오면 13번 핀(또는 칩LED)가 점멸함, 'b'는 12번, 'c'는 11번 핀을 점멸함  
- arduino/robot_hands.ino : 'a'가 넘어오면 바위, 'b'가 넘어오면 보자기, 'c'가 넘어오면 가위를 내는 로봇팔 제어 프로그램  

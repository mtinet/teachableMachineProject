# teachableMachineProject

###### 파이썬(3.8.6까지 구동 확인)에 tensorflow(2.3.1까지 구동 확인), PIL(pillow), opencv-python, pyserial 라이브러리를 설치해 사용함  

#### 0. 관련 링크  
- [Teachable Machine](https://teachablemachine.withgoogle.com/)  
- [관련 영상](https://photos.app.goo.gl/G8MU8mmxGLo6pj2D9)  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/example.png?raw=true)  

#### 1. 개요  
- 로컬에서 웹캠 영상을 가져와서 학습된 모델의 레이블에 있는 클래스를 정규화된 비율로 출력함  
- 정규화된 특정 결과값의 비중(0.7 이상)에 따라 시리얼 통신으로 utf-8의 형태의 'a', 'b', 'c'를 송신함  
- 송신된 데이터에 의해 동작하는 간단한 Arduino 파일을 첨부함  
- 아두이노 파일(dataReceiveTest.ino)은 'a'가 들어오면 13번핀을, 'b'가 들어오면 12번핀을, 'c'가 들어오면 11번핀을 제어하도록 프로그래밍되어 있음  
- 아두이노 파일(robot_hands_three servo.ino)은 3개의 서보모터를 사용하여 'a'가 들어오면 rock을, 'b'가 들어오면 paper를, 'c'가 들어오면 scissors를 내도록 프로그래밍되어 있음  
- 아두이노 파일(dataReceiveTest.ino)은 2개의 서보모터를 사용하여 'a'가 들어오면 paper를, 'b'가 들어오면 scissors를, 'c'가 들어오면 rock을 내도록 프로그래밍되어 있음 

#### 2. 프로젝트 깃허브 레파지토리 다운로드  
- 브라우저를 열고 [github.com/mtinet/teachableMachineProject](github.com/mtinet/teachableMachineProject)로 이동  
- github 레파지토리의 오른쪽 상단에 있는 code 버튼을 클릭함  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/download1.png?raw=true)  
- 방법 1 : Download ZIP 버튼을 눌러 프로젝트 폴더를 다운로드 하고 원하는 작업폴더로 이동해 압축을 해제하고 사용함  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/download2.png?raw=true)  

- 방법 2 : 주황색 동그라미 안의 버튼을 눌러 레파지토리 주소를 복사하고 cmd의 git clone을 이용해 다운로드(압축을 풀 필요가 없으나 [git이 미리 설치](https://git-scm.com/)되어 있어야 함)  
```
git clone https://github.com/mtinet/teachableMachineProject.git
```

#### 3. python 설치  
- tensorflow는 아직 python 3.8.X까지만 지원을 하므로, 파이썬을 3.9버전이 설치되어 있을 경우 3.8.X이하 버전으로 재설치해야 함  
- python.org사이트 Download-Windows에서 Python 3.8.X- Sept. 24, 2020 카테고리 안에 있는 Download Windows x86-64 executable installer를 다운로드 받아 설치함, [링크](https://www.python.org/downloads/windows/)  
- python 설치할 때는 Add python 3.8 to PATH를 반드시 체크하고 설치를 진행하세요  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/python.png?raw=true)  

#### 4. cmd창을 열고 프로젝트 폴더로 이동  
- 다운로드 한 폴더를 열고 주소를 복사함
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/location1.png?raw=true)  
- 윈도우의 돋보기에서 cmd 를 실행함  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/cmd.png?raw=true)  
- 아래 명령어를 통해 프로젝트 폴더로 이동
```
cd "다운로드 한 폴더 위치" 
```
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/location2.png?raw=true)  
- 아래 명령어를 실행하면서 발생하는 오류를 확인하고 해당하는 라이브러리를 설치함
```
python teachableMachineByVideo.py
```

#### 5. 라이브러리 설치  
- tensorflow 설치
```{.python} 
pip install tensorflow
```
- termcolor 설치
```{.python} 
pip install termcolor
```
- PIL 설치  
```{.python} 
pip install pillow 
```
- pyserial 설치
```{.python} 
pip install pyserial
```
- opencv-python 설치
OpenCV의 main module만 사용한다면 아래처럼 설치
```{.python} 
pip install opencv-python
```
만약 main module과 extra module을 같이 사용하고 싶다면 아래처럼 설치합니다.
```{.python} 
pip install opencv-contrib-python  
```
- 그 외 오류는 오류나는 부분을 카피해서 구글에 물어보면 해답을 얻을 수 있음  
 
#### 6. 파일 구동은 아래 명령어로 하면 됨, 프로그램 정지는 'q'버튼  
```{.python}  
$python teachableMachineByVideo.py  
```  

#### 7. 결과 이미지  
- teachable machine에서 class를 입력하지 않을경우 자동 생성된 class이름으로 나옴  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/test.png?raw=true)  

- 가위바위보가 잘 학습되었을 경우 아래와 같은 화면이 나오면서 serial통신을 통해 a, b, c의 문자를 송신하게 됨  
![](https://github.com/mtinet/teachableMachineProject/blob/master/image/scissors.png?raw=true)  
주의사항 : 가위바위보와 결과 속의 얼굴은 서로 무관하고, 학습시킬 때 나눈 클래스의 총 합계 퍼센트가 늘 100%가 나오는 것임, 어떤 화면이 입력되건 총 합계는 100%라는 말. 학습을 잘 시키는 것도 중요하고, 디폴트값을 넣어주는 것도 중요하다는 사실을 알 수 있음  


#### 8. 그 외 파일들의 기능은 다음과 같다.  
- keras_model.h5 : teachable machine 홈페이지에서 Export한 모델파일, 이 파일이 머신러닝 학습의 결과이며, 이 파일을 이용해 학습된 내용을 활용함, 현재는 파란색, 흰색, 초록색을 구분하는 모델파일이 올라가 있음. 티처블 머신으로 자신이 학습시키고자 하는 이미지를 학습시키면 됨  
- labels.txt : 모델을 만들 때 레이블을 몇개로 해 학습을 시켰느냐에 따라 label이 나뉨, label 이름을 자신이 원하는 것으로 수정해 학습시키면 추후 모델로 추론을 할 때 그 label이 표시됨, 물론 나중에 다운로드 받은 labels.txt 파일을 직접 수정해도 무관함  
- teachableMachineByVideo.py : 학습된 모델 파일로 웹캠에서 입력되는 영상을 분석하여 추론해주는 파이썬 파일, 이 파일이 이 프로젝트의 핵심, 추후 라즈베리파이에 탑재해서 로봇을 제어하는데 사용할 예정  
- arduino/dataReceive.ino : 학습된 데이터를 기반으로 추론한 결과가 특정 퍼센티지를 넘을 때 바이트 형태의 데이터를 전송하는데, 그 때 아두이노에서 데이터가 잘 받아지는지를 확인하는 코드, 'a'가 바이트의 형태로 잘 넘어오면 13번 핀(또는 칩LED)가 점멸함, 'b'는 12번, 'c'는 11번 핀을 점멸함  
- arduino/robot_hands.ino : 'a'가 넘어오면 바위, 'b'가 넘어오면 보자기, 'c'가 넘어오면 가위를 내는 로봇팔 제어 프로그램  

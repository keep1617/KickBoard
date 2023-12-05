KickBoard return judging System
===

<p align="center">
</p>

킥보드 return judging 시스템을 위한 code와 mp3 파일을 포함하고 있습니다.
저희가 구현한 것은 반납 시스템 전부가 아니라 
지정된 구역 안에 주차되었는지 판별하는 시스템입니다.
지정구역은 파란색으로 색칠되어 있다고 가정합니다.




* [Models](#models)
* [Setup](#install)
* [Set Usb port](#setting)
* [Reference](#reference)

<a name="models"></a>
## Models

파이썬 코드를 통해 UI를 구현하고 반납 버튼을 누른다면 RGB와 GPS 센서에서 값을 불러옵니다.
JUDGING 클래스에서 이를 처리하고 반납 여부를 알려줍니다.


<a name="install"></a>
## Setup

1. Module과 python 버전
  python = 3.10.9
  pygame = 2.5.2
  tkinter = 8.6
  numpy =1.23.5
  serial=3.5

Ubuntu 20.04 기준 설치 방법


Conda 가상환경 설치되어있다고 가정합니다

2. Install pip
  '''
  conda create -name <name> python=3.10.9
  '''


   

   
     

   



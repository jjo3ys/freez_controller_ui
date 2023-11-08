<div align='center'>
<h1> 🖥️ Refrigerator simulator 🖥️</h1>
<h3> 인천대학교 냉방기 시뮬레이터 </h3>

![Alt text](/img/image.png)

<h3> 🥶인천대학교 냉방 시스템을 효율적으로 제어하기 위해<br>
냉방기 제어 데이터, 날씨 등을 사용하여 DQN으로 학습한 모델을 시각적으로 보여주기 위한 UI입니다.</h3>
</div>

<br>

## 🛠️ Stacks

<img src="https://img.shields.io/badge/-python-05122A?style=flat&logo=python"/>
<img src="https://img.shields.io/badge/-pytorch-05122A?style=flat&logo=pytorch"/>

<br>

## ✨ 화면 구성

| 1. 메인 화면           | 2. 그래프 화면 |
|---------------------|---|
| ![Alt text](/img/image.png) |![Alt text](/img/image-1.png)|

<br>

## ✨ 시연 영상

!['ui'](sample/video1438827884.gif)

## ✨ 구현 내용
- UI 디자인 및 제작
- DQN 모델 연동

## ✨ 주요 기능

### 1. 수온에 따른 색깔 변화
![Alt text](/img/image-2.png)
냉매를 전달하는 파이프에 온도 변화를 시각적으로 표현했습니다. <br>

> 섭씨 7도에서 17도를 구간으로 나누어 각 구간별로 공급·환수 온도에 따라 색을 다르게 했습니다.

### 2. 스크롤을 통한 날짜 이동 및 재생 속도 배율
![Alt text](/img/image-3.png)

데이터의 날짜의 이동을 편하게 하기 위해 횡스크롤을 구현했습니다. <br>
시뮬레이터의 재생 속도를 변화할 수 있도록 구현했습니다.

### 3. 그래프 구현

데이터의 변화를 쉽게 비교하기 위해 6가지의 그래프를 구현했습니다. 


## ✨ 후기

하나 부터 열까지 다 직접 ui를 제작해 보면서 개발한 프로그램을 눈으로 볼 수 있었기에 백엔드와는 또 다른 재미를 느꼈습니다.<br>
해당 프로젝트로 디지털 트윈 아이디어 경진대회에 참가했었고, 대학원/일반 부분에서 대상을 수상했습니다. <br>
심사위원 분께서 시뮬레이터를 보시고 가장 디지털 트윈에 걸맞는 프로젝트라 말씀해주셨던게 가장 기억에 남았습니다. <br>

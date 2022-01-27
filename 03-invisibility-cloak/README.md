# Invisibility Cloak

이 구현은 아래 영상의 구현에 기반합니다.<br/>
https://www.youtube.com/watch?v=suytB_6aS6M

Summary: https://noisyblue.notion.site/Week3-b5920ba379a54c9aac04eb3fb755e9b4

여기 있는 코드는 파이썬 3.9.9 에서 테스트 됐습니다.

# 실행 전 dependencies 설치

pip install -r requirements.txt

# 파일 설명

## original 디렉토리

영상의 원본 구현체입니다.

## segmentation_based 디렉토리

원본 구현에 영감을 받아 Instance segmentation 으로 사람을 정교하게 잘라내면, 책을 들고 있으면 책만 둥둥 떠 다니는 것처럼 표현할 수 있겠다 싶어 재미삼아 시도해 본 구현입니다.

### 실행 전에
> [PointRend 모델 파일](https://github.com/ayoolaolafenwa/PixelLib/releases/download/0.2.0/pointrend_resnet50.pkl) 을 다운로드 받아 segmentation_based 디렉토리에 복사해야 함.

### - camera.py
간단한 Camera preview callback 기능을 구현해 놓은 클래스 입니다.<br/>
Vision 관련 작업을 할 때 불필요하게 반복되는 카메라 관련 코드를 간소화 하기 위해 작성 했습니다.<br/>
이전의 구현에 더해 CameraFrameHandler.on_stop callback 을 추가 했습니다.

### - segment_and_mask.py
첫 60 프레임은 원본 구현과 마찬가지로 배경 저장을 하고, 카메라로부터 입력을 받아 Instance segmentation 을 실행한 뒤에 사람만 제거 합니다.
CPU 에서는 inference 속도가 엄청나게 느려 실시간으로 구동하기 어렵습니다.


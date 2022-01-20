# FU mosaic

이 구현은 아래 영상의 구현에 기반합니다.<br/>
https://www.youtube.com/watch?v=tQeuPrX821w

Summary: https://noisyblue.notion.site/Week2-9c4b9ebdac5947b0800441c1e640e157

여기 있는 코드는 파이썬 3.9.9 에서 테스트 됐습니다.

# 실행 전 dependencies 설치

pip install -r requirements.txt

# 파일 설명

## original 디렉토리

영상의 원본 구현체입니다.

## dnn_classifier

원본에서 사용된 각 landmarks 사이의 각도 features 와 달리 landmarks 의 scaled 좌표 feature set 을 가지고 시도하면 어떻게 될지 알아보기 위해 Neural-net 기반
binary classifier 를 가지고 시도해 본 디렉토리입니다.<br /><br/>
2000 여개의 훈련 세트로 훈련을 했는데, 훈련 과정에서 모델이 over-fitted 되는 문제를 해결하지 못한 상황이고 이의 해결이 과제로 남아 있습니다.

### - camera.py

간단한 Camera preview callback 기능을 구현해 놓은 클래스 입니다.<br/>
Vision 관련 작업을 할 때 불필요하게 반복되는 카메라 관련 코드를 간소화 하기 위해 작성 했습니다.<br/>
camera.test.py 를 확인해 보면 사용법을 알 수 있습니다.

### - sample_collector.py

DNN 기반 classifier 의 train sample 들을 모으기 위한 스크립트입니다. samples.csv 는 개인적으로 모아 본 positive 샘플(FU)과 negative 샘플들입니다.

### - classifier_train.py

주어진 training samples 로 FU binary classifier 를 학습하기 위한 모델 training 용 스크립트입니다.

### - fu_filter.py

훈련한 binary classifier 를 가지고 FU 를 모자이크 처리하는 inference 스크립트입니다.  

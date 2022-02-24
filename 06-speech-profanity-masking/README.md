# Speech Profanity masking

이 구현은 아래 영상의 구현에 기반합니다.<br/>
https://www.youtube.com/watch?v=J01pGSPOQTk

Summary: https://noisyblue.notion.site/Week6-f706ae9154584f54bbc45e6534b998b4

여기 있는 코드는 파이썬 3.9.9 에서 테스트 됐습니다.

# 실행 전 dependencies 설치

MacOS 의 경우
> brew install ffmpeg

> pip install -r requirements.txt

# 파일 설명

## beep_generator.test.py

Config 를 조정해 가며 beep 음을 만들고 play 하고 plotting 해 볼 수 있는 테스트 스크립트

## main.py

욕설 masking 을 시험해 볼 수 있는 스크립트.<br/>
> python main.py recognizer-type recognition-target-uri original-audio-path

- recognizer-type: 인식기 타입
    - GCP: GCP STT 를 이용한 인식. 구현 안됨;
    - AWS: AWS Transcribe 를 이용한 인식.
    - MOCK: 테스트 용도의 mock result 를 리턴하는 mock recognizer
- recognition-target-uri: 인식할 오디오 파일이 올려져 있는 각 STT vendor 의 static storage 상의 URL.<br />recognizer-type 이 MOCK인 경우 아무
  문자나 입력.
- original-audio-path: 로컬 드라이브 상의 원본 오디오 파일

## recognizers 디렉토리

음성인식 API wrapper 구현을 모아 놓은 디렉토리 

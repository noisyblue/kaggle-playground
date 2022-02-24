from recognizers.speech_recognizer import SpeechRecognizer, SpeechRecognitionResult, SpeechSegment


class MockRecognizer(SpeechRecognizer):
    def recognize(self, sound_file_uri: str) -> SpeechRecognitionResult:
        return SpeechRecognitionResult(full_text="일어나이 씨발놈아 개새끼야 야이 개 같은 년아 씨발년아 씨발년아",
                                       segments=[
                                           SpeechSegment(text="일어나", start_millis=0, end_millis=1000),
                                           SpeechSegment(text="이", start_millis=1000, end_millis=1100),
                                           SpeechSegment(text="씨발놈아", start_millis=1100, end_millis=2000),
                                           SpeechSegment(text="개새끼야", start_millis=2000, end_millis=3000),
                                           SpeechSegment(text="야", start_millis=3000, end_millis=3900),
                                           SpeechSegment(text="이", start_millis=3900, end_millis=4100),
                                           SpeechSegment(text="개", start_millis=4100, end_millis=7400),
                                           SpeechSegment(text="같은", start_millis=7400, end_millis=7500),
                                           SpeechSegment(text="년아", start_millis=7500, end_millis=7900),
                                           SpeechSegment(text="씨발년아", start_millis=7900, end_millis=9800),
                                           SpeechSegment(text="씨발년아", start_millis=9800, end_millis=11400),
                                       ])

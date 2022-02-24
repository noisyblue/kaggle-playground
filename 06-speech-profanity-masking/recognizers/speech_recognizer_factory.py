from enum import Enum

from .aws_transcribe_recognizer import AWSTranscribeRecognizer
from .mock_recognizer import MockRecognizer
from .speech_recognizer import SpeechRecognizer


class SpeechRecognizerType(Enum):
    GCP = "GCP",
    AWS = "AWS",
    MOCK = "MOCK",


class SpeechRecognizerFactory:
    @staticmethod
    def get_recognizer(type: SpeechRecognizerType) -> SpeechRecognizer:
        if type == SpeechRecognizerType.GCP:
            raise NotImplementedError()
        elif type == SpeechRecognizerType.AWS:
            return AWSTranscribeRecognizer()
        elif type == SpeechRecognizerType.MOCK:
            return MockRecognizer()
        else:
            raise RuntimeError(f'Unsupported type: {type}')

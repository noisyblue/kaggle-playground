import abc
from dataclasses import dataclass
from typing import List


@dataclass
class SpeechSegment:
    text: str
    start_millis: int
    end_millis: int


@dataclass
class SpeechRecognitionResult:
    full_text: str
    segments: List[SpeechSegment]


class SpeechRecognizer:
    @abc.abstractmethod
    def recognize(self, sound_file_uri: str) -> SpeechRecognitionResult:
        raise NotImplementedError()

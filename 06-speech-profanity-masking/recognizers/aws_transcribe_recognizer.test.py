#!/usr/bin/env python3
import dataclasses
import json

from aws_transcribe_recognizer import AWSTranscribeRecognizer

recognizer = AWSTranscribeRecognizer()
result = recognizer.recognize("s3://test-stt-noisyblue/sound_short.mp3")

print(json.dumps(dataclasses.asdict(result), ensure_ascii=False, indent=2))

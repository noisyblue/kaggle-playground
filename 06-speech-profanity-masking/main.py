#!/usr/bin/env python3
import sys
from os import path

from pydub import AudioSegment

from beep_generator import BeepGenerator, BeepConfig
from recognizers.speech_recognizer_factory import SpeechRecognizerFactory, SpeechRecognizerType

SWEAR_WORDS = ['씨발', '개새끼']


def create_beep(duration_millis: int):
    beep_config = BeepConfig(duration_millis=duration_millis,
                             freq=1000,
                             volume=0.5)
    beep_signal = BeepGenerator.create_beep(beep_config)

    return AudioSegment(
        beep_signal.tobytes(),
        frame_rate=beep_config.sample_rate,
        sample_width=beep_signal.dtype.itemsize,
        channels=1
    )


def mask(recognizer_type: SpeechRecognizerType, recog_target_uri: str, original_audio_path: str):
    recognizer = SpeechRecognizerFactory.get_recognizer(recognizer_type)
    result = recognizer.recognize(recog_target_uri)

    swear_segments = list(
        filter(lambda segment: any(swear_word in segment.text for swear_word in SWEAR_WORDS), result.segments))

    sound = AudioSegment.from_file(original_audio_path, format='mp3')
    mixed_sound = sound

    for swear_segment in swear_segments:
        beep = create_beep(swear_segment.end_millis - swear_segment.start_millis)
        mixed_sound = mixed_sound.overlay(beep, position=swear_segment.start_millis, gain_during_overlay=-40)

    splitted_file_name = path.splitext(path.basename(original_audio_path))
    mixed_sound.export(splitted_file_name[0] + ".result." + recognizer_type.name.lower() + splitted_file_name[1],
                       format='mp3')


if len(sys.argv) < 4:
    print(f'usage: {sys.argv[0]} GCP|AWS|MOCK recognition-target-uri original-audio-path')
    exit(-1)

mask(SpeechRecognizerType[sys.argv[1]], sys.argv[2], sys.argv[3])

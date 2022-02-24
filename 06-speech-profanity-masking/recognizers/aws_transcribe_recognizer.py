import time
import uuid

import boto3
import requests

from recognizers.speech_recognizer import SpeechRecognizer, SpeechRecognitionResult, SpeechSegment


class AWSTranscribeRecognizer(SpeechRecognizer):
    def recognize(self, sound_file_uri: str) -> SpeechRecognitionResult:
        transcribe = boto3.client('transcribe', region_name="ap-northeast-2")

        job_name = str(uuid.uuid1())
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={
                'MediaFileUri': sound_file_uri
            },
            MediaFormat='mp3',
            LanguageCode='ko-KR'
        )

        while True:
            job_result = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            if job_result['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            print("Waiting for AWS Transcribe result...")
            time.sleep(5)

        if job_result['TranscriptionJob']['TranscriptionJobStatus'] == 'FAILED':
            raise RuntimeError("AWS transcribe job failed!")

        transcript_file_url = job_result['TranscriptionJob']['Transcript']['TranscriptFileUri']
        res = requests.get(transcript_file_url)

        return self.to_recognition_result(res.json())

    def to_recognition_result(self, transcribe_result) -> SpeechRecognitionResult:
        full_text = transcribe_result['results']['transcripts'][0]['transcript']

        segments = list(
            map(lambda item: SpeechSegment(text=item['alternatives'][0]['content'],
                                           start_millis=float(item['start_time']) * 1000,
                                           end_millis=float(item['end_time']) * 1000),
                transcribe_result['results']['items'])
        )

        return SpeechRecognitionResult(full_text=full_text, segments=segments)

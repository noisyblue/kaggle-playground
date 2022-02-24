from datetime import datetime

from dateutil.tz import tzlocal

{
    'TranscriptionJob': {
        'TranscriptionJobName': 'cd8178f0-94ba-11ec-ae45-acde48001122',
        'TranscriptionJobStatus': 'COMPLETED',
        'LanguageCode': 'ko-KR',
        'MediaSampleRateHertz': 44100,
        'MediaFormat': 'mp3',
        'Media': {
            'MediaFileUri': 's3://test-stt-noisyblue/sound_short.mp3'
        },
        'Transcript': {
            'TranscriptFileUri': 'https://s3.ap-northeast-2.amazonaws.com/aws-transcribe-ap-northeast-2-prod/926348855347/cd8178f0-94ba-11ec-ae45-acde48001122/f13c339c-6c0b-4b74-9ced-3370cbf165dc/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aDmFwLW5vcnRoZWFzdC0yIkcwRQIgSn9jYF1%2BMYgyZ%2FszrJes667pOfo2C%2FQl9Xu7FtEx5ysCIQDEEQMF8RBWd2HiAI79XdMsju1RNkInEq2%2F%2Fk4I1SR4fiqEBAh3EAMaDDQzNTc2MzIxMDc3NiIMFerTsmHxkwFJPeBUKuEDsMyaEuEsoy3nLYQHE43TkLhM3JyC1cY7pW0MMOEy7VJnF4AIqChERkJOAVZSDkdYPoWlRdWl7qgCOVkxuEvgo6JmLUmgA0FgkWws%2FTsOh1C%2FoPcPmYu42dPeS%2BatuXrExVw747li%2Bh%2BJkbN7fKuXAdGlsgY%2FLmQoAzsifNN2UFRhfNmkg3lCcDoF0YPQnBQxa57861oFto5jqG3vmZQMNZjiG3d%2F5RLeupNVJniMHBFBAWZ7RZnQ8lGPEIdZBveuttyAeAXTdlsiKJf1ecUCY7nxVxdkzD5Ta6wEtNfwmfeE159P%2FrhawyrtgSEBvcJo7xRaWvU3lszjYXgyAEGxEtbI%2Flggr8idkwshVti2aqPiwJCvhGpaTAnXYRiiDRVINDyRVpcQRNIFspn%2Ff3PgYnNo04s0%2BkW3htiQlSv6knZpFeIExFjNO2n60i%2FqMR2MaGceYMIkzomFJEUSw3Sq23%2BARxgf%2BV2F5900dnDdofoeNyOcxZnwbaCbe3ulnAd1wSafJlrg%2FvtRGG8fMa1QlsRK%2B5w2AS6ESl3oWLzvUYWd42Y7OFqIcb0ovAI7PmePnc4yhsHgqKpbd%2FRg%2Fqh7tlG1K6jSwvkLFgE6NDeyifD7ysGbGl4SDengTiGxWXOdNjDPgtmQBjqlAY92cqvAp3NbymlShP3WOlDtLvIE0YmOPE%2FXHMME5vIdfClBs6xVFW4LQlX8kqfs7KZGIPCG6yh4MzP2pgonUtBP%2BmBANFyxFApCEjmlj1EmX9QMzez2x4n8kw06aFQsTDXdDTqxBqABP4uf6n0P2L23iYi7LwfZ%2FF%2BtRxJOWo2SoMteJ4vOX7cINqPglfiuBDG43ULZQVg0Mqm5xOLWWMQVEflUHQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220223T151118Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIAWK5MC5IMJ4RFX4EE%2F20220223%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=f0db0f78fd188f170a2d95ee3a1412ad4ef4c868d7a6fb6c136e087482e4f385'
        },
        'StartTime': datetime.datetime(2022,
                                       2,
                                       24,
                                       0,
                                       10,
                                       57,
                                       681000,
                                       tzinfo=tzlocal()),
        'CreationTime': datetime.datetime(2022,
                                          2,
                                          24,
                                          0,
                                          10,
                                          57,
                                          628000,
                                          tzinfo=tzlocal()),
        'CompletionTime': datetime.datetime(2022,
                                            2,
                                            24,
                                            0,
                                            11,
                                            15,
                                            407000,
                                            tzinfo=tzlocal()),
        'Settings': {
            'ChannelIdentification': False,
            'ShowAlternatives': False
        }
    },
    'ResponseMetadata': {
        'RequestId': 'e8c6cc93-b27f-41f7-9bc9-b5486b55ba85',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'content-type': 'application/x-amz-json-1.1',
            'date': 'Wed, 23 Feb 2022 15:11:18 GMT',
            'x-amzn-requestid': 'e8c6cc93-b27f-41f7-9bc9-b5486b55ba85',
            'content-length': '2052',
            'connection': 'keep-alive'
        },
        'RetryAttempts': 0
    }
}

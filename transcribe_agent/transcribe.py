import argparse
import io

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "api-key.json")


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    # from google.api_core.protobuf_helpers import get_messages
    from google.cloud import speech
    # from google.cloud.speech import enums
    from google.cloud.speech_v1 import types
    # from google.cloud.speech import types

    client = speech.SpeechClient(credentials=credentials)

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=types.RecognitionConfig.AudioEncoding.FLAC,
        enable_word_time_offsets=True,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.long_running_recognize(config=config, audio=audio)

    # response = client.recognize(config=config, audio=audio)
    return response.results


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient(credentials=credentials)

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

# print(transcribe_file("../audio_files/abc.m4a"))

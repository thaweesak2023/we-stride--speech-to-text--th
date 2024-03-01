# docs-link: https://cloud.google.com/speech-to-text/v2/docs/batch-recognize

# batch recognition on multiple files
import re
from typing import List

from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

import os

# TODO: change path to your service key.json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..path/key.json"


def transcribe_batch_multiple_files_v2(
    project_id: str,
    gcs_uris: List[str],
    gcs_output_path: str,
) -> cloud_speech.BatchRecognizeResponse:
    """Transcribes audio from a Google Cloud Storage URI.

    Args:
        project_id: The Google Cloud project ID.
        gcs_uris: The Google Cloud Storage URIs to transcribe.
        gcs_output_path: The Cloud Storage URI to which to write the transcript.

    Returns:
        The BatchRecognizeResponse message.
    """
    # Instantiates a client
    client = SpeechClient()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        # language_codes=["en-US"],
        language_codes=["th-TH"],
        model="long",
    )

    files = [
        cloud_speech.BatchRecognizeFileMetadata(uri=uri)
        for uri in gcs_uris
    ]

    request = cloud_speech.BatchRecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        files=files,
        recognition_output_config=cloud_speech.RecognitionOutputConfig(
            gcs_output_config=cloud_speech.GcsOutputConfig(
                uri=gcs_output_path,
            ),
        ),
    )

    # Transcribes the audio into text
    operation = client.batch_recognize(request=request)

    print("Waiting for operation to complete...")
    # response = operation.result(timeout=120)
    response = operation.result(timeout=12000)

    print("Operation finished. Fetching results from:")
    for uri in gcs_uris:
        file_results = response.results[uri]
        print(f"  {file_results.uri}...")
        output_bucket, output_object = re.match(
            r"gs://([^/]+)/(.*)", file_results.uri
        ).group(1, 2)

        # Instantiates a Cloud Storage client
        storage_client = storage.Client()

        # Fetch results from Cloud Storage
        bucket = storage_client.bucket(output_bucket)
        blob = bucket.blob(output_object)
        results_bytes = blob.download_as_bytes()
        batch_recognize_results = cloud_speech.BatchRecognizeResults.from_json(
            results_bytes, ignore_unknown_fields=True
        )

        for result in batch_recognize_results.results:
            print(f"     Transcript: {result.alternatives[0].transcript}")

    return response

# TODO: change your google cloud project id and gcs_uris
gs_out = 'gs://gg-tts-v202402/out-tts-audio'
gs_in_list = [
    'gs://gg-tts-v202402/in-tts-audio/yt-THE--STANDARD.wav',
    # '...',
]

transcribe_batch_multiple_files_v2(
    'your-project-id',
    gs_in_list,
    gs_out,
)

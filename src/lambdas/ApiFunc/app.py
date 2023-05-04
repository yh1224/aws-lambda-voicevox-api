import base64
import io
import os
from tempfile import NamedTemporaryFile
from urllib import parse

from pydub import AudioSegment
from voicevox_core import VoicevoxCore, AccelerationMode

SPEAKER_ID = 0

core = VoicevoxCore(
    acceleration_mode=AccelerationMode.AUTO,
    open_jtalk_dict_dir=os.environ["OPEN_JTALK_DICT_DIR"],
)
core.load_model(SPEAKER_ID)


def lambda_handler(event, context):
    body = base64.b64decode(event["body"]).decode("utf-8")
    query = parse.parse_qs(body)
    texts = query.get("text")
    if not texts or len(texts) == 0:
        return {
            "statusCode": 422,
        }
    text = texts[0]
    print(f"text: {text}")

    mp3 = wav_to_mp3(get_voice(text))
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "audio/mp3",
        },
        "body": base64.b64encode(mp3),
        "isBase64Encoded": True,
    }


def get_voice(text: str) -> bytes:
    audio_query = core.audio_query(text, SPEAKER_ID)
    return core.synthesis(audio_query, SPEAKER_ID)


def wav_to_mp3(wav: bytes) -> bytes:
    with NamedTemporaryFile() as f:
        AudioSegment.from_wav(io.BytesIO(wav)).export(f.name, format="mp3")
        return f.read()

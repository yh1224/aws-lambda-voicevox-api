import base64
import ctypes
import os
from pathlib import Path
from urllib import parse

from pydub import AudioSegment

VOICEBOX_DIR = "voicevox_core-linux-x64-cpu-0.14.3"
OPEN_JTALK_DICT_DIR = "open_jtalk_dic_utf_8-1.11"
ctypes.cdll.LoadLibrary(os.getcwd() + f"/{VOICEBOX_DIR}/libvoicevox_core.so")
ctypes.cdll.LoadLibrary(os.getcwd() + f"/{VOICEBOX_DIR}/libonnxruntime.so.1.13.1")
from voicevox_core import VoicevoxCore

ACCELERATION_MODE = "AUTO"
SPEAKER_ID = 0

core = VoicevoxCore(
    acceleration_mode=ACCELERATION_MODE,
    open_jtalk_dict_dir=OPEN_JTALK_DICT_DIR,
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

    voice = get_voice(text)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "audio/mp3",
        },
        "body": base64.b64encode(voice),
        "isBase64Encoded": True,
    }


def get_voice(text: str) -> bytes:
    audio_query = core.audio_query(text, SPEAKER_ID)
    wav = core.synthesis(audio_query, SPEAKER_ID)
    Path("/tmp/voice.wav").write_bytes(wav)
    AudioSegment.from_wav("/tmp/voice.wav").export("/tmp/voice.mp3", format="mp3")
    with open("/tmp/voice.mp3", "rb") as f:
        return f.read()

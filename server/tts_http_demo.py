#coding=utf-8

'''
requires Python 3.6 or later
pip install requests
'''
import base64
import json
import uuid
import requests

appid = ""
access_token= ""
cluster = "volcano_tts"
voice_type = "BV001_streaming"
host = "openspeech.bytedance.com"
api_url = f"https://{host}/api/v1/tts"
header = {"Authorization": f"Bearer;{access_token}"}

request_json = {
    "app": {
        "appid": appid,
        "token": access_token,
        "cluster": cluster
    },
    "user": {
        "uid": "388808087185088"
    },
  "audio": {
        "voice_type": "BV001_streaming",
        "encoding": "mp3",
        "compression_rate": 1,
        "rate": 24000,
        "speed_ratio": 1.0,
        "volume_ratio": 1.0,
        "pitch_ratio": 1.0,
        "emotion": "happy",
        "language": "cn"
    },
    "request": {
        "reqid": "uuid",
        "text": "字节跳动语音合成",
        "text_type": "plain",
        "operation": "query",
        "silence_duration": "125",
        "with_frontend": "1",
        "frontend_type": "unitTson",
        "pure_english_opt": "1"
    }
}

if __name__ == '__main__':
    try:
        print(f"request body: \n{request_json}")
        resp = requests.post(api_url, json.dumps(request_json), headers=header)
        print(f"resp body: \n{resp.json()}")
        if "data" in resp.json():
            data = resp.json()["data"]
            file_to_save = open("test_submit.mp3", "wb")
            file_to_save.write(base64.b64decode(data))
    except Exception as e:
        e.with_traceback()


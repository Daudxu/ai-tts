from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import base64
import json
from fastapi.responses import JSONResponse

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
        "encoding": "wav",
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

app = FastAPI()

# 配置字节跳动 TTS 相关信息
APP_ID = "3530645641"
ACCESS_TOKEN = "7CqJznCCgzekQLgfBajDlHwBTMsLuMcQ"
CLUSTER = "volcano_tts"
VOICE_TYPE = "BV001_streaming"
API_URL = "https://openspeech.bytedance.com/api/v1/tts"

# 定义请求格式
class TTSRequest(BaseModel):
    text: str


@app.get("/")
async def hello():
    return {
        "message": "Hello World"
    }

@app.post("/tts")
async def generate_tts():
    resp = requests.post(api_url, json.dumps(request_json), headers=header)
        # print(f"resp body: \n{resp.json()}")
    if "data" in resp.json():
            data = resp.json()["data"]
            return data

 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)

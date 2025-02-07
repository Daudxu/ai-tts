import uuid
import requests
import hashlib
import time

# 有道 API 相关信息
YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = ''
APP_SECRET = ''

def encrypt(signStr):
    """
    对签名串进行 SHA-256 加密
    :param signStr: 签名串
    :return: 加密后的签名
    """
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def truncate(q):
    """
    对输入的文本进行截断处理
    :param q: 输入的文本
    :return: 截断后的文本
    """
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

def do_request(data):
    """
    发送 POST 请求到有道 API
    :param data: 请求数据
    :return: 响应对象
    """
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def connect():
    # 待翻译的文本
    q = "Hello, world!"
    # 源语言，例如 'en' 表示英语
    source_language = 'en'
    # 目标语言，例如 'zh-CHS' 表示中文简体
    target_language = 'zh-CHS'
    # 用户词表 ID，若没有可留空
    vocab_id = ""

    data = {}
    data['from'] = source_language
    data['to'] = target_language
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = vocab_id

    try:
        response = do_request(data)
        response.raise_for_status()  # 检查请求是否成功
        content_type = response.headers.get('Content-Type')

        if content_type == "audio/mp3":
            # 生成音频文件名
            millis = int(round(time.time() * 1000))
            file_path = f"audio_{millis}.mp3"
            try:
                with open(file_path, 'wb') as fo:
                    fo.write(response.content)
                print(f"音频已保存到 {file_path}")
            except Exception as e:
                print(f"保存音频文件时出错: {e}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"请求出错: {e}")

if __name__ == '__main__':
    connect()
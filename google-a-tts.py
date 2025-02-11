import os
from google.cloud import texttospeech

# 初始化客户端
client = texttospeech.TextToSpeechClient()

# 设置文本和合成请求参数
synthesis_input = texttospeech.SynthesisInput(ssml="""
<speak>
    <phoneme alphabet="ipa" ph="tʃə">cher</phoneme>
</speak>
""")

# 设置语音参数，指定语音为 en-US
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O"  # 选择美国英语的某个语音样式
)
# 设置语音参数，指定语音为 en-GB    
# voice = texttospeech.VoiceSelectionParams(
#     language_code="en-GB",
#     name="en-GB-Studio-B"  # 选择英国国英语的某个语音样式
# )

# 设置音频配置
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# 合成语音
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# 保存合成的语音文件
with open("output_ssml_teacher.mp3", "wb") as out:
    out.write(response.audio_content)

print("Audio content written to file 'output_ssml_teacher.mp3'")

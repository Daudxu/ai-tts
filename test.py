import os

# 获取 GOOGLE_APPLICATION_CREDENTIALS 环境变量的值
# $env:GOOGLE_APPLICATION_CREDENTIALS="D:\key\mythic-lattice-450500-i8-aa5f989b2d1a.json"
# echo $env:GOOGLE_APPLICATION_CREDENTIALS

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if credentials_path:
    print(f"Credentials file found at: {credentials_path}")
else:
    print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")

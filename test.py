import os

# 获取 GOOGLE_APPLICATION_CREDENTIALS 环境变量的值
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if credentials_path:
    print(f"Credentials file found at: {credentials_path}")
else:
    print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")

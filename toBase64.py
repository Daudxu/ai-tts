import base64

def read_and_print_mp3_as_base64(file_path):
    try:
        with open(file_path, 'rb') as file:  # 以二进制模式打开文件
            mp3_data = file.read()  # 读取文件内容
            base64_data = base64.b64encode(mp3_data).decode('utf-8')  # 将二进制数据转换为Base64编码的字符串
            print(base64_data)  # 打印Base64编码的字符串
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 假设脚本位于当前工作目录，并且a.mp3也在该目录下
mp3_file_path = 'hello.mp3'
read_and_print_mp3_as_base64(mp3_file_path)
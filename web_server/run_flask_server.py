import subprocess

def run_flask_server():
    """Flask 서버를 실행하는 함수"""
    subprocess.run(['python', 'web_server/flask_server.py'], check=True)
    print("Flask 서버가 실행되었습니다.")

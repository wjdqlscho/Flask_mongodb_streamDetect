# Flask 서버 Dockerfile
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /usr/src/web_server

# requirements.txt 복사
COPY requirements.txt ./

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 서버 파일 복사
COPY flask_server.py ./
COPY templates/ ./templates/

# 실행 명령
CMD ["python", "flask_server.py"]

FROM python:3.9-slim

# 기본 패키지 설치
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# tmp 디렉토리 생성
RUN mkdir -p tmp

# 포트 9000 노출
EXPOSE 9000

# 애플리케이션 실행
CMD ["python", "server.py"]

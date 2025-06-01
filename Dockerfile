# 1. Ubuntu 최신 버전 사용
FROM ubuntu:latest

# 2. 필수 패키지 설치
RUN apt-get update && apt-get install -y git python3 python3-pip python3-venv

# 3. 작업 디렉토리 생성 및 전체 파일 복사
WORKDIR /app
COPY . /app

# 4. 가상 환경 생성 및 패키지 설치
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r /app/requirements.txt

# 5. 컨테이너 실행 시 main.py 실행
CMD ["/app/venv/bin/python", "/app/main.py"]

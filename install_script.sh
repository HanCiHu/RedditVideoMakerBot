#!/bin/bash

# FFmpeg 설치
brew install ffmpeg

# Python 3.10 설치
brew install python@3.10

# 가상 환경 설정
python3.10 -m venv .venv

# 가상 환경 활성화
source .venv/bin/activate

# 필요한 패키지 설치
pip install -r requirements.txt

# Playwright 설치 및 의존성 패키지 설치
python -m playwright install
python -m playwright install-deps

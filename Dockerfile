# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /bot/

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "run.sh"]
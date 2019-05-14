FROM python:slim-stretch

WORKDIR /speech_recognition

COPY . /speech_recognition

RUN apt-get update && apt-get install -y swig gcc git libpulse-dev \
libasound2-dev wget && \ 
rm -rf /var/lib/apt/lists/* && \
pip install --upgrade pip -r requirements.txt
RUN wget https://de.ifmo.ru/--openedu/dataprocessing/appliedai/audio5/1.wav

CMD ["python", "app.py"]

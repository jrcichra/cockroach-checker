FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y python-lxml python-requests && rm -rf /var/lib/apt/lists/* 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY cockroach.py .
COPY main.py .
ENTRYPOINT ["/app/main.py"]

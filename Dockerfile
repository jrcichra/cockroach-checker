FROM debian:10
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip python3-lxml python3-requests && rm -rf /var/lib/apt/lists/* 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY cockroach.py .
COPY main.py .
ENTRYPOINT ["/app/main.py"]

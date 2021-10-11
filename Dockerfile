FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libxml2 libxslt1-dev && rm -rf /var/lib/apt/lists/* 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY cockroach.py .
COPY main.py .
ENTRYPOINT ["/app/main.py"]

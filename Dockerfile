FROM python:3.10-alpine3.14
WORKDIR /app
RUN apk add gcc libxml2 libxslt-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY cockroach.py .
COPY main.py .
ENTRYPOINT ["/app/main.py"]

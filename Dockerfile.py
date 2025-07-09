FROM debian:stable-slim
RUN apt-get update && apt-get install -y python3 python3-pip
COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]
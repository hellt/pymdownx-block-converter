FROM python:3.11-slim

WORKDIR /app

COPY block_conv.py /app/block_conv.py

CMD ["python", "/app/block_conv.py"]

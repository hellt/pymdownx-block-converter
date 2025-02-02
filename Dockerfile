FROM python:3.11-slim

WORKDIR /app

COPY block-conv.py /app/block-conv.py

CMD ["python", "/app/block-conv.py"]

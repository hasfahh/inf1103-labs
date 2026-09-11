FROM python:3.11-slim

WOKRDIR /app

COPY auditor.py .

CMD ["python", "auditor.py"]
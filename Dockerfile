FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir psutil

COPY monitoring_script.py .

CMD ["python", "-u", "monitoring_script.py"]
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model/afgan-generator.keras .
COPY server .

EXPOSE 38880

CMD ["python", "main.py"]
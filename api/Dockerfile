# api/Dockerfile

FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY vision_requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r vision_requirements.txt

COPY models/greenvision_model ./models/greenvision_model

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
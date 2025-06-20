
FROM python:3.10

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y poppler-utils tesseract-ocr && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

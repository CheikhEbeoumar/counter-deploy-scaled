FROM python:3.11-slim

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

EXPOSE 5000
# For simplicity use the Flask dev server (or switch to gunicorn in production)
CMD ["python","app.py"]
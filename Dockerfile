FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies (kept minimal) and clean up apt caches
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential gcc \
	&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Create a non-root user and give ownership of the app directory
RUN groupadd -r app && useradd -r -g app app \
	&& chown -R app:app /app

USER app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]


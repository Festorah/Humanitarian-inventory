FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Copy your project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install celery[redis]

# Expose the port the app runs on
EXPOSE 8000

# Start the Celery worker
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]

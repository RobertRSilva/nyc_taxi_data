# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir numpy==1.21.6 pandas==1.3.5 duckdb==0.10.0 requests==2.31.0 pyarrow==13.0.0

# Copy the application code
COPY src/ .

# Command to run the main script
CMD ["python", "main.py"]
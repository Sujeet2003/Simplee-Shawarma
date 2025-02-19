# Use a minimal Python base image
FROM python:3.11-alpine

# Set environment variables to reduce image size
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a directory for the app
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code after installing dependencies
COPY . .

# Expose the port for the application
EXPOSE 8000

# Use exec form to avoid potential issues with signals
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

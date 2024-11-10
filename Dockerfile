# Start from an official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /app/venv && \
    . /app/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Python application code into the container
COPY . .

# Activate the virtual environment and run the script
CMD ["/bin/bash", "-c", "source /app/venv/bin/activate && python AppPy.py"]


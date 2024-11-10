# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY AppPy.py .

# Run the Python script when the container launches
CMD ["python", "AppPy.py"]


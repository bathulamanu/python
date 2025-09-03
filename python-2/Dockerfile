# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy Python script into container
COPY hello_world_2_server.py /app

# Install Flask
RUN pip install flask

# Expose port 9091
EXPOSE 9091

# Run the Python app
CMD ["python", "hello_world_2_server.py"]

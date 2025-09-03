# Use official Python image
FROM python:3.12-slim

WORKDIR /app

# Copy Python script
COPY hello_world_4.py /app

# Install Flask
RUN pip install flask

# Expose port 9093
EXPOSE 9093

# Run the app
CMD ["python", "hello_world_4.py"]

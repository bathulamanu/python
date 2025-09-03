FROM python:3.12-slim
WORKDIR /app

# Copy Python script
COPY hello_world_3.py /app

# Install Flask
RUN pip install flask

# Expose port 9092
EXPOSE 9092

# Run the app
CMD ["python", "hello_world_3.py"]

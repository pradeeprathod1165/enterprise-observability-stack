# Pull a base image
FROM python:3.9-slim

# create work directory
WORKDIR /app

# install packages
RUN pip install prometheus_client

# Copy app.py to work directory 
COPY app.py .

# Expose Port
EXPOSE 8080 8000

# RUN
CMD ["python", "app.py"]

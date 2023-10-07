# Use an official Python runtime as the parent image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (on your machine) to the container at /app
COPY . /app/

# Install required packages

RUN apt-get update && apt-get install -y netcat && apt-get clean

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for the app to listen on
EXPOSE 8000

# # Command to run on container start
# CMD ["gunicorn", "message_service.wsgi:application", "--bind", "0.0.0.0:8000"]

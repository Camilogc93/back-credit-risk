#FROM python:3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Set the working directory to /app

WORKDIR /app


RUN pip install --upgrade pip

COPY ./app/requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
#COPY requirements.txt .
RUN pip install -r requirements.txt
#requirements.txt
#COPY ./app /app
# Make port 80 available to the world outside this container

# Copy the current directory contents into the container at /app
COPY ./app /app/

EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--forwarded-allow-ips","'*'"]
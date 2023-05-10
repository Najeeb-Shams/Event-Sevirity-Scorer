# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN python setup.py bdist_wheel
# Make port 8000 available to the world outside this container
EXPOSE 5291
# EXPOSE 5432
# Define environment variable
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1


# install the PostgreSQL development headers and libraries on the Docker container.
RUN apt-get update && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:5290"]

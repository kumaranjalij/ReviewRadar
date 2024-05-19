# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install system-level dependencies
RUN apt-get update \
    && apt-get install -y pkg-config \
                          libmariadb-dev-compat \
                          gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import nltk; nltk.download('vader_lexicon')"

RUN python -m spacy download en_core_web_sm

# Copy the rest of the application code into the container at /app
COPY . /app/

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]


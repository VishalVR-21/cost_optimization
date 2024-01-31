# Use the official Python image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the local script and requirements to the container
COPY s3_script.py /app/
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python", "main.py"]
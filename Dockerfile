# Use the official Python image
FROM python:3.9

# Install system packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 5100

# Command to run the Flask application
CMD ["python", "app.py"]
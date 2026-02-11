# Use a Python image that matches your local version (3.13)
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to take advantage of Docker caching
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files from your computer into the container
# (Ensure you have a .dockerignore to skip the 'myenv' folder)
COPY . .

# The command to run your tests when the container starts
CMD ["behave", "Features/Registration.feature"]
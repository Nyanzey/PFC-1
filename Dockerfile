# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local project files to the container (optional)
# COPY . .

# Set the default command to a shell
CMD ["bash"]

# Use the official nvidia/cuda base image with Python 3.9
FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel

# Set the working directory
WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Copy the requirements into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to a shell
CMD ["bash"]

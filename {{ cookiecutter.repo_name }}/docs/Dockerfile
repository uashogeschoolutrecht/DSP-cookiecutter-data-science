# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /docs

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the MkDocs configuration and documentation files
COPY . .

# Command to serve the MkDocs site on container startup
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# app is exposed on port 8080
EXPOSE 8080

# Run app.py when the container launches
ENTRYPOINT ["python3"]
CMD ["app.py"]

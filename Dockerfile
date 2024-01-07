FROM python:3.9.18-alpine

# Set the working directory to /app
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D appuser
USER appuser

# app is exposed on port 8080
EXPOSE 8080

# Run app.py when the container launches

CMD ["python3", "app.py"]

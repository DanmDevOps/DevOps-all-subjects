# Step 1: Use Python 3.9 as the base image
FROM python:3.9

# Step 2: Set environment variables to prevent writing pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire application into the container
COPY . /app/

# Step 6: Expose port 5000 for Flask
EXPOSE 5000

# Step 7: Run Flask using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]

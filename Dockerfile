# 1. Base Image: Use the specific Python version you requested
# We use 'slim' to keep the image size small
FROM python:3.12.6-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first (for better caching)
COPY requirements.txt .

# 4. Install dependencies
# --no-cache-dir reduces image size by not saving download cache
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code into the container
COPY . .

# 6. Expose the port (Cloud Run typically uses 8080)
EXPOSE 8080

# 7. Define the command to start the app
# Note: You will need to change 'app_blue:app' depending on which color you are building
CMD ["uvicorn", "app_purple:app", "--host", "0.0.0.0", "--port", "8080"]

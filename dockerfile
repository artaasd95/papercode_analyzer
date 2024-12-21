# Use the official lightweight Python image.
# You can specify a specific version (e.g., python:3.10-slim) if you prefer.
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install pipenv or update pip if you want; here, we’ll just stick with pip:
RUN pip install --upgrade pip

# Copy requirements first, install packages
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the FastAPI source code
COPY app/ /app/

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Start FastAPI using uvicorn
# If your main application is in main.py and your FastAPI instance is named `app`,
# change the module name accordingly (e.g., `app.main:app` if you have a main.py inside app folder).
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

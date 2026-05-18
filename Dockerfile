# Use an official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files to the container
COPY requirements.txt .
COPY app.py .
COPY RF_trained_model.pkl .
COPY cleanned_data.csv .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
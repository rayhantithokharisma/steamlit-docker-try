# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install Streamlit and other dependencies
RUN pip install --no-cache-dir streamlit scikit-learn joblib

# Copy the Streamlit app into the container
COPY streamlit_iris.py .
COPY iris_model.pkl .

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_iris.py"]

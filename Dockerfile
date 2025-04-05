FROM python:3.12-slim # choose a lightweight official base image
WORKDIR /app  # set a working directory in the container, it will be created if it doesn't exist
COPY requirements.txt . # First copy the project's requirements to leverage Docker's caching mechanism
RUN pip install --no-cache-dir -r requirements.txt # install necessary dependencies without unnesessary caching
COPY . . # copy other application files to the container
EXPOSE 8000 # expose the app on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] # run the app with uvicorn

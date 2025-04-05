# choose a lightweight official base image
FROM python:3.12-slim 

# set a working directory in the container, it will be created if it doesn't exist
WORKDIR /app  

# First, copy the project's requirements to leverage Docker's caching mechanism to the work directory
COPY requirements.txt .

# install necessary dependencies without unnesessary caching
RUN pip install --no-cache-dir -r requirements.txt 

# copy other application files to the container
COPY . . 

# expose the app on port 8000
EXPOSE 8000 

# run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 

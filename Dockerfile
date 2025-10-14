#python image
FROM python:3.11-slim    

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code and models
COPY src/ src/
COPY model/ model/

# expose port 8080
EXPOSE 8080

# start the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
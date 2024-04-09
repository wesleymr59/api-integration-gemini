# - Dockerfile configurations
FROM python:3.11.2-alpine3.16
LABEL DESCRIPTION="ia-gemini-api" 
COPY requirements.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /usr/src
COPY . .
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8090"]

# docker image build -t ia-gemini-api:latest .

# docker container run --rm -it -v $(pwd):/usr/src --env-file .env -p 8090:8090 --name ia-gemini-api ia-gemini-api:latest
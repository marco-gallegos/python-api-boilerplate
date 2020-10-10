FROM python:3.8

LABEL MAINTAINER="TTL2020B"
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "api.py"]
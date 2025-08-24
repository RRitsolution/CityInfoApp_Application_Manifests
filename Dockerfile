##Base python image
FROM python:3.11-slim



##Working directory

WORKDIR /app


##Copy requirements.txt

COPY requirements.txt .


## Install dependencies

RUN pip install -r requirements.txt



##Copy entire app

COPY . .


## Expose flask port

EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]

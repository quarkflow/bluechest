FROM python:3.9
WORKDIR /usr/src/bluechest
COPY bluechest/ .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]

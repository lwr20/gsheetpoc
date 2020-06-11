FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test.py .

ENTRYPOINT python test.py
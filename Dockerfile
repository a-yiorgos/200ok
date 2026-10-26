FROM python:3.12-slim

# Create a non-root user and set permissions
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY 200ok.py .

RUN chown -R appuser:appuser /usr/app

USER appuser

EXPOSE 8080

ENTRYPOINT ["python", "200ok.py"]

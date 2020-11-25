FROM python:3.7
RUN pip install --no-cache-dir bottle
WORKDIR /usr/app
COPY 200ok.py .
CMD [ "python", "200ok.py" ]

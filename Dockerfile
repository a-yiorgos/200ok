FROM python:3.7
RUN pip install --no-cache-dir bottle
CMD [ "python", "200ok.py" ]

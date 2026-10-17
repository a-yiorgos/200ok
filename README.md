# 200ok

A simple FastAPI application that returns HTTP 200 JSON responses on every GET and POST request it receives.

## Features

- Built with **FastAPI** and **uvicorn**
- Handles GET and POST requests on any URL path
- Returns JSON payload with timestamp, server hostname, and requested path
- Listens on port `8080` by default, or the port specified in the `PORT` environment variable
- Dockerized with rootless user support on Python 3.12

## Running Locally

### Prerequisites

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Default port (8080):

```bash
python 200ok.py
```

Custom port using `PORT` environment variable:

```bash
PORT=9090 python 200ok.py
```

## Running with Docker

Build the Docker image:

```bash
docker build -t 200ok .
```

Run the container:

```bash
docker run -p 8080:8080 200ok
```

Run on a custom port inside container:

```bash
docker run -e PORT=8080 -p 8080:8080 200ok
```

## Deployment Example

```bash
kubectl create deployment http200ok --image yiorgos/200ok
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

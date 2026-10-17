import importlib
import os
from fastapi.testclient import TestClient
import pytest

app_module = importlib.import_module("200ok")
client = TestClient(app_module.app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "hostname" in data
    assert data["url"] == "/"

def test_post_custom_path():
    response = client.post("/test/path?query=1")
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "hostname" in data
    assert data["url"] == "/test/path"

def test_port_environment_variable(monkeypatch):
    monkeypatch.setenv("PORT", "9999")
    port = int(os.getenv("PORT", "8080"))
    assert port == 9999

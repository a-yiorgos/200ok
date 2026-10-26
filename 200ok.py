import argparse
import os
import platform
import time
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

parser = argparse.ArgumentParser(description="200ok HTTP server")
parser.add_argument("--text", type=str, help="Optional text to include in response payload")
args, _ = parser.parse_known_args()
RESPONSE_TEXT = args.text

app = FastAPI()

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
async def catch_all(request: Request, full_path: str):
    path = request.url.path
    datum = {
        "date": datetime.now(timezone.utc).isoformat(),
        "timestamp": time.time(),
        "hostname": platform.node(),
        "url": path,
    }
    if RESPONSE_TEXT is not None:
        datum["text"] = RESPONSE_TEXT
    return JSONResponse(content=datum)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)

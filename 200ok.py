import os
import platform
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.api_route("/{full_path:path}", methods=["GET", "POST"])
async def catch_all(request: Request, full_path: str):
    path = request.url.path
    datum = {
        "date": datetime.now(timezone.utc).isoformat(),
        "hostname": platform.node(),
        "url": path,
    }
    return JSONResponse(content=datum)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)

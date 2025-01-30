from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
# import uvicorn

# Email Address
EMAIL = "ayodejioni1505@gmail.com"
# API Repo Link
GITHUB_URL = "https://github.com/Ayo-Oni-515/stage-0-backend.git"

# API Response
data = {
    "email": EMAIL,
    "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "github_url": GITHUB_URL
}

#FastAPI instace creation
app = FastAPI()

# print(uvicorn)

# CORS Management
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["GET"],  
    allow_headers=["*"]
)

@app.get('/')
async def index():
    return data
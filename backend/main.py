
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Recurrex Deep-Shield 360")

# Allow the frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "team": "Recurrex", "project": "Deep-Shield 360"}

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    # This is the endpoint where the video will be sent
    return {
        "filename": file.filename,
        "verdict": "Processing...",
        "confidence": "Scanning Biometrics"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
  

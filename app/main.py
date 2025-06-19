from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.ocr_utils import parse_transcript
from app.evaluator import evaluate_transcript

app = FastAPI(title="TSU Transfer Evaluation Test Platform")

@app.post("/upload")
async def upload_transcript(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    transcript_data = await parse_transcript(file)
    results = evaluate_transcript(transcript_data)
    return JSONResponse(content=results)

@app.get("/")
def read_root():
    return {"message": "✅ FastAPI is running on Render!"}

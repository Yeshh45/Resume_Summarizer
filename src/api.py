from fastapi import FastAPI, HTTPException, UploadFile, File
from src.extract_text import extract_resume_text
from src.summarizer import gpt_summarizer

app = FastAPI()

@app.post("/summarize/")
async def summarize_resume(file: UploadFile = File(...)):
    try:
        # Extract text from the uploaded resume file
        resume_text = extract_resume_text(file.file)

        # Generate summary using GPT-based method
        summary = gpt_summarizer(resume_text)
        
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

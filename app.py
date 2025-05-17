from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict
from functions import generate_sse_events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    url: str
    # documents will be handled separately with Form and File

class ResponseBody(BaseModel):
    layer: Literal[1, 2, 3, 4] = Field(..., description="Validation layer number (1 to 4)")
    task_name: str = Field(..., description="Name of the validation task")
    sub_task_name: Optional[str] = Field(None, description="Name of the sub-task")
    status: Literal['pass', 'fail', 'processing', 'finished'] = Field(..., description="Validation status")
    message: Optional[str] = Field(None, description="Short summary of the result")
    data: Optional[Dict] = Field(None, description="Detailed validation report or metrics")

@app.post("/stream")
async def stream(url: str = Form(...), documents: Optional[UploadFile] = None):
    """
    Stream validation events to the client using SSE.
    """
    # Process the URL and documents if provided
    data = {
        "url": url
    }
    
    if documents:
        # Here you would handle the document processing
        # For now, we'll just acknowledge it
        data["documents"] = documents.filename
    
    # Return a streaming response with the validation events
    return StreamingResponse(
        generate_sse_events(data),
        media_type="text/event-stream"
    )

@app.get("/")
async def root():
    return {"message": "ContentQA API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import APIRouter, HTTPException,UploadFile, File
from doctor_resume_parser.doctor_helper_functions.dr_halper import get_doctor_resume_data
import os
import uuid
router = APIRouter()

UPLOAD_DIR = "doctor_resume"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Read file content
        content = await file.read()
        
        # Sanitize filename and generate unique name
        original_filename = os.path.basename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{original_filename}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)
        
        # Save file to target directory
        with open(file_path, "wb") as f:
            f.write(content)
        
        # Process the file
        result = await get_doctor_resume_data(file_path)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router.get("/health")
async def health_check():
    """
    Simple health-check endpoint.
    """
    return {"status": "healthy"}

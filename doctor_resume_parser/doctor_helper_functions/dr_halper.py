import os
import asyncio
import json
from pydantic import ValidationError
from doctor_resume_parser.doctor_schema_model.doctor_model import FinalResponse
from reader_function.pdf_reader import extract_text_from_pdf_async
from llm.llm import get_chat_model
# File: doctor_resume_parser/doctor_helper_functions/exceptions.py

class ResumeValidationError(Exception):
    """Exception raised for validation errors in the resume."""
    pass

class ResumeProcessingError(Exception):
    """Exception raised for errors during resume processing."""
    pass
# File: doctor_resume_parser/doctor_helper_functions/helper_functions.py
def cleanup_file(path: str):
    """Synchronous file cleanup function"""
    if os.path.exists(path):
        os.remove(path)

async def get_doctor_resume_data(file_path: str) -> FinalResponse:
    llm = await get_chat_model()
    tmp_path = file_path 
    try:
        #text = await asyncio.to_thread(extract_text_from_pdf, file_path)
        # In your processing function:
        text = await extract_text_from_pdf_async(file_path)
        structured_llm =  llm.with_structured_output(FinalResponse, method="function_calling")
        parsed_resume = await structured_llm.ainvoke(text)
        parsed_resume = parsed_resume.model_dump_json()
        return json.loads(parsed_resume)
    except ValidationError as e:
        raise ResumeValidationError(f"Invalid resume format: {str(e)}") from e
    except Exception as e:
        raise ResumeProcessingError(f"Processing failed: {str(e)}") from e
    finally:
        # Async-safe file cleanup that executes regardless of success or failure
        await asyncio.to_thread(cleanup_file, tmp_path)

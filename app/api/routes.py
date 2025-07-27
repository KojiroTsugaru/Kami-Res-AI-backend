from fastapi import APIRouter, HTTPException
from app.api.schemas import PromptRequest, PromptResponse
from app.utils.prompt_service import process_parameters
from app.utils.openai_service import get_openai_response_from_image
import base64

router = APIRouter()

@router.post("/generate-response", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    try:
        # Generate prompt text
        response = process_parameters({"mood": request.mood, "length": request.length})
        prompt = response["prompt"]
        
        # Decode base64 image and call OpenAI API
        image_bytes = base64.b64decode(request.image_base64)
        openai_response = get_openai_response_from_image(image_bytes, prompt)
        
        return {
            "status": "success",
            "data": openai_response,
            "code": 200
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
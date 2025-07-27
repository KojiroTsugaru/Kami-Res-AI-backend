from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    mood: str
    length: float
    image_base64: str = Field(description="Base64-encoded image data (required)")

class PromptResponse(BaseModel):
    status: str
    data: dict
    code: int 
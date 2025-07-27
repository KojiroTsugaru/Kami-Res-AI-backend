# Kami-Res-AI FastAPI Backend

## Running the Server

Install dependencies:
```
pip install -r requirements.txt
```

Run the FastAPI server:
```
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /api/v1/prompt` - Generate a prompt or get a response from OpenAI with an image.

## Example Request

```
curl -X POST "http://localhost:8000/api/v1/prompt" \
  -H "Content-Type: application/json" \
  -d '{
    "mood": "casual",
    "length": 1.0,
    "image_base64": null
  }'
```

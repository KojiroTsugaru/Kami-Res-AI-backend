import os
import requests
import base64
import logging
from typing import Any, Dict

# Configure logger (customize as needed)
logger = logging.getLogger(__name__)

class OpenAIImageError(Exception):
    """Custom exception class for errors during image-based requests."""
    pass

base_url = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o"
max_tokens = 1000

def get_openai_response_from_image(image_bytes: bytes, prompt: str) -> Dict[str, Any]:
    api_key = os.getenv("OPENAI_ACCESS_TOKEN")
    if not api_key:
        raise OpenAIImageError("Environment variable OPENAI_ACCESS_TOKEN is not set")

    # 1. Base64 encode the image
    try:
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
    except Exception as e:
        raise OpenAIImageError(f"Failed to Base64-encode image: {e}")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": max_tokens
    }

    try:
        # 2. Execute the request with a timeout
        response = requests.post(base_url, headers=headers, json=payload, timeout=15)
        # 3. Raise an exception for HTTP status errors
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logger.exception("OpenAI API request timed out")
        raise OpenAIImageError("OpenAI API request timed out")
    except requests.exceptions.HTTPError as http_err:
        # Catch 4xx/5xx HTTP errors here
        status = http_err.response.status_code if http_err.response else None
        text = http_err.response.text if http_err.response else ""
        logger.error(f"OpenAI API HTTPError {status}: {text}")
        raise OpenAIImageError(f"OpenAI API error: HTTP {status} {text}")
    except requests.exceptions.RequestException as req_err:
        # Catch any other network-related RequestException here
        logger.exception("Exception occurred during OpenAI API request")
        raise OpenAIImageError(f"OpenAI API request failed: {req_err}")

    try:
        # 4. Parse JSON response
        return response.json()
    except ValueError as json_err:
        logger.exception("Failed to parse response JSON")
        raise OpenAIImageError(f"Response JSON parsing error: {json_err}")

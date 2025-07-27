import os
import requests
import base64

base_url = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o"
max_tokens = 1000

def get_openai_response_from_image(image_bytes, prompt):
    """
    Sends an image and prompt to the OpenAI API and returns the full response.
    Args:
        image_bytes (bytes): The image data in bytes.
        prompt (str): The prompt text.
    Returns:
        dict: The full OpenAI API response.
    Raises:
        Exception: If the API call fails or returns an error.
    """
    api_key = os.getenv("OPENAI_ACCESS_TOKEN")
    if not api_key:
        raise Exception("OPENAI_ACCESS_TOKEN not set in environment.")

    # Convert image to base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o",
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

    response = requests.post(base_url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"OpenAI API error: {response.status_code} {response.text}")
    return response.json()


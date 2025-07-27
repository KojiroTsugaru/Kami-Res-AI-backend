# Kami-Res-AI Backend API

A FastAPI-powered backend service for an AI-powered image analysis and response generation application. This project demonstrates modern backend development practices, API design, and integration with OpenAI's vision models.

## 🚀 Project Overview

Kami-Res-AI Backend is a RESTful API service that processes images and generates contextual responses based on user-defined moods and length preferences. It integrates with OpenAI's GPT-4 Vision model to analyze images and generate appropriate text responses.

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python 3.11+)
- **Server**: Uvicorn (ASGI)
- **AI Integration**: OpenAI GPT-4 Vision API
- **Testing**: pytest with FastAPI TestClient
- **Deployment**: Railway
- **Documentation**: Auto-generated OpenAPI/Swagger docs

## ✨ Features

- **Image Analysis**: Process base64-encoded images using OpenAI's vision capabilities
- **Mood-Based Responses**: Generate responses in different tones (casual, humorous, cool, romantic, formal, empathetic)
- **Length Control**: Specify response length (short, medium, long)
- **RESTful API**: Clean, well-documented endpoints
- **Error Handling**: Comprehensive error responses and validation
- **Async Support**: Built with FastAPI's async capabilities

## 📚 API Documentation

### Base URL
```
https://your-railway-app.railway.app/api/v1
```

### Endpoints

#### POST `/generate-response`
Generates an AI response based on an image and configuration.

**Request Body:**
```json
{
  "mood": "casual",
  "length": 1.0,
  "image_base64": "base64_encoded_image_data"
}
```

**Parameters:**
- `mood` (string, required): Response tone - `casual`, `humorous`, `cool`, `romantic`, `formal`, `empathetic`
- `length` (float, required): Response length - `1.0` (short), `2.0` (medium), `3.0` (long)
- `image_base64` (string, required): Base64-encoded image data

**Response:**
```json
{
  "status": "success",
  "data": {
    "choices": [
      {
        "message": {
          "content": "Generated response text..."
        }
      }
    ]
  },
  "code": 200
}
```

**Error Responses:**
- `400`: Invalid parameters (mood, length)
- `422`: Missing required fields
- `500`: Server error (API key issues, OpenAI errors)

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API key

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kami-res-ai-backend
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   echo "OPENAI_ACCESS_TOKEN=your_openai_api_key_here" > .env
   ```

5. **Run the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   - API: http://localhost:8000/api/v1/generate-response
   - Interactive docs: http://localhost:8000/docs
   - OpenAPI spec: http://localhost:8000/openapi.json

### Testing

Run the test suite:
```bash
pytest -v
```

Run with coverage:
```bash
pytest --cov=app -v
```

## 🏗️ Project Structure

```
kami-res-ai-backend/
├── app/
│   ├── api/
│   │   ├── routes.py          # API endpoints
│   │   └── schemas.py         # Pydantic models
│   ├── data/
│   │   └── prompts.py         # Prompt templates
│   ├── utils/
│   │   ├── openai_service.py  # OpenAI API integration
│   │   └── prompt_service.py  # Prompt processing
│   └── main.py               # FastAPI application
├── tests/
│   └── test_api.py           # API tests
├── requirements.txt          # Python dependencies
├── nixpacks.toml            # Railway deployment config
└── README.md                # This file
```

## 🚀 Deployment

This project is configured for deployment on Railway:

1. **Connect your repository** to Railway
2. **Set environment variables** in Railway dashboard:
   - `OPENAI_ACCESS_TOKEN`: Your OpenAI API key
3. **Deploy automatically** - Railway will use `nixpacks.toml` for configuration

The app will be available at your Railway-provided URL.

## 🔧 Development

### Code Quality
- **Type Hints**: Full type annotation support
- **Pydantic Models**: Request/response validation
- **Error Handling**: Comprehensive exception handling
- **Testing**: Unit tests with pytest and FastAPI TestClient

### Key Implementation Details

#### FastAPI Features Used
- **Pydantic Models**: For request/response validation
- **Dependency Injection**: For service layer integration
- **Async Endpoints**: For better performance
- **Auto-generated Documentation**: OpenAPI/Swagger integration

#### OpenAI Integration
- **Vision API**: GPT-4 Vision model for image analysis
- **Base64 Encoding**: Image data processing
- **Error Handling**: Graceful API error management

## 📝 License

This project is part of a portfolio showcase. Feel free to use as reference for your own projects.

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome!

---

**Built with ❤️ using FastAPI and OpenAI API**

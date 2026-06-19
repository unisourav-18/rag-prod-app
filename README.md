# RAG PDF Chat Application

A production-style Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, index their contents into a vector database, and ask natural language questions based on the document content.

## Features

* Upload and process PDF documents
* Automatic document chunking for efficient retrieval
* Vector search powered by Qdrant
* Semantic document retrieval using embeddings
* AI-powered question answering
* Streamlit web interface
* FastAPI backend
* Event-driven workflows with Inngest

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Inngest

### Vector Database

* Qdrant

### Document Processing

* LlamaIndex PDF Reader
* SentenceSplitter

### AI & Embeddings

* Google Gemini API
* Embedding-based semantic search

## Project Structure

```text
rag-prod-app/
│
├── main.py                 # FastAPI + Inngest functions
├── streamlit_app.py        # Streamlit frontend
├── data_loader.py          # PDF loading and chunking
├── vector_db.py            # Qdrant operations
├── custom_types.py         # Pydantic models
├── .env                    # Environment variables
├── requirements.txt
└── README.md
```

## How It Works

### 1. PDF Ingestion

* User uploads a PDF document.
* The PDF is parsed using LlamaIndex.
* Content is split into smaller chunks.
* Embeddings are generated.
* Chunks are stored in Qdrant.

### 2. Question Answering

* User submits a question.
* The question is converted into an embedding.
* Relevant document chunks are retrieved from Qdrant.
* Retrieved context is passed to the language model.
* The model generates an answer grounded in the document.

## Local Setup

### Clone Repository

```bash
git clone https://github.com/unisourav-18/rag-prod-app.git
cd rag-prod-app
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Start Qdrant

```bash
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

### Run FastAPI Backend

```bash
uv run uvicorn main:app --reload
```

### Run Inngest Dev Server

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest
```

### Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

## Future Improvements

* Multi-document support
* Source citation highlighting
* Chat history persistence
* User authentication
* Cloud-hosted vector database
* Streaming responses
* Document management dashboard

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Event-Driven Architectures
* FastAPI Development
* Streamlit Deployment
* PDF Processing Pipelines
* AI Application Development

## Author

**Sourav Pandey**

Aspiring Software Engineer & Game Developer passionate about AI applications, backend systems, and modern software development.

## License

This project is intended for educational and portfolio purposes.

# Enterprise RAG Chatbot

## Overview

The Enterprise RAG Chatbot is a Retrieval-Augmented Generation (RAG) application that enables users to upload documents and ask natural language questions about their content. The application retrieves the most relevant document chunks from a Pinecone vector database and generates context-aware responses using Groq's Llama 3.3 70B model.

The project follows a modular architecture with separate components for document ingestion, chunking, embeddings, vector storage, retrieval, and response generation.

---

## Features

- Upload and process PDF, DOCX, TXT, Excel, and image files
- OCR support for image-based documents
- Semantic search using vector embeddings
- Pinecone vector database integration
- Context-aware answer generation using Groq Llama 3.3 70B
- Source chunk retrieval for grounded responses
- Configurable chunking and retrieval parameters
- Modular and extensible project structure
- Streamlit-based user interface

---

## System Architecture

### Document Ingestion Pipeline

```
                Upload Document
                       │
                       ▼
              DocumentLoader
                       │
                       ▼
                  Text Chunking
         (1000 chars, 200 overlap)
                       │
                       ▼
      Generate Embeddings (MiniLM-L6-v2)
                       │
                       ▼
          Store Embeddings in Pinecone
```

---

### Question Answering Pipeline

```
                 User Question
                       │
                       ▼
           Pinecone Similarity Search
                 (Top 5 Results)
                       │
                       ▼
             Retrieve Relevant Chunks
                       │
                       ▼
       Build Context + Conversation History
                       │
                       ▼
         Groq Llama 3.3 70B Versatile
                       │
                       ▼
          Generate Answer + Source Chunks
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| UI | Streamlit |
| LLM | Groq - Llama 3.3 70B Versatile |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | Pinecone |
| OCR | Tesseract OCR |
| Configuration | Python dotenv |

---

## Project Structure

```
Enterprise-RAG/
│
├── chat/
├── chunking/
├── embeddings/
├── ingestion/
├── llm/
├── rag/
├── tests/
├── utils/
├── vectorstore/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Siva0387-tech/enterprise-rag.git
cd enterprise-rag
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root and configure:

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
PINECONE_API_KEY=YOUR_PINECONE_API_KEY

PINECONE_INDEX_NAME=enterprise-rag
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
LLM_MODEL=llama-3.3-70b-versatile
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Workflow

1. Upload a supported document.
2. The document is loaded and split into chunks.
3. Embeddings are generated.
4. Embeddings are stored in Pinecone.
5. Ask questions about the uploaded document.
6. Relevant chunks are retrieved from Pinecone.
7. Groq Llama generates an answer using the retrieved context.

---

## Future Enhancements

- Multi-document knowledge base
- Metadata filtering
- Hybrid search
- Re-ranking
- Conversation memory improvements
- Authentication and user management
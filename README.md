# 🚀 Lenny Growth Assistant

## 📌 Overview
The Lenny Growth Assistant is a full-stack AI-powered web application designed to help Product Managers and Growth teams extract actionable insights from Lenny’s Podcast transcripts.

It provides grounded answers, generates structured long-form content, and simulates a retrieval-augmented generation (RAG) system while remaining lightweight and easy to deploy.

---

## ✨ Features

- 💬 **Conversational Q&A**
  - Ask product and growth-related questions
  - Get grounded answers based on transcript data

- 📚 **Context-Aware Retrieval (RAG-style)**
  - Retrieves relevant transcript snippets
  - Displays sources for transparency

- ✍️ **Ship 30–style Content Generation**
  - Generates structured articles with:
    - Hooks
    - Insights
    - Action plans
    - Clear takeaways

- 🧠 **Session-Based Interaction**
  - Maintains conversation context per session

- ⚙️ **Health Monitoring**
  - `/health` endpoint for system status

- 🧪 **Artifact Output**
  - Generates markdown-style structured content

---

## 🏗️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML + JavaScript
- **Architecture:** Lightweight RAG-inspired system
- **Data:** Simulated transcript dataset

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install fastapi uvicorn

Supports grounded responses with citation-style context.

## Architecture

- FastAPI backend
- In-memory session handling
- Simple RAG retrieval (keyword-based)
- HTML frontend with API integration

## Limitations

- No PostgreSQL (used in-memory due to time constraint)
- No real LLM (mock responses)
- Basic retrieval (no embeddings)

## Future Improvements

- Add PostgreSQL + pgvector
- Integrate Ollama / OpenAI
- Improve UI with React
- Add authentication
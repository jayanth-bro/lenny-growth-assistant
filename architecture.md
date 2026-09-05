# 🏗️ Architecture

## 📌 Overview
Lenny Growth Assistant is a lightweight full-stack system designed to extract insights from podcast transcripts using a FastAPI backend and a simple web frontend.

---

## 🧩 Components

### 🔹 Backend (FastAPI)
- Handles API requests and logic
- Endpoints:
  - `/api/chat` → Q&A + article generation
  - `/api/session` → session creation
  - `/health` → system status

---

### 🔹 Frontend (HTML + JS)
- Simple UI for user interaction
- Sends requests via REST API
- Displays responses and articles

---

### 🔹 Retrieval Layer (RAG-style)
- Keyword-based matching
- Retrieves relevant transcript chunks
- Simulates RAG system

---

### 🔹 Session Layer
- In-memory dictionary
- Stores chat history per session

---

### 🔹 Data Layer
- Static transcript dataset (Python list)
- No external DB

---

### 🔹 Model Layer
- Rule-based responses
- Placeholder for LLM integration

---

## 🔄 Flow

1. User enters query  
2. Frontend sends request  
3. Backend retrieves context  
4. Response/article generated  
5. Sent back to UI  

---

## ⚖️ Trade-offs
- No embeddings → less accuracy  
- No database → not scalable  
- No LLM → static responses  

---

## 🚀 Future
- PostgreSQL + pgvector  
- LLM integration  
- Better UI (React)  
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime
import logging

# ✅ CORS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lenny Growth Assistant")

# ✅ Logging (professional touch)
logging.basicConfig(level=logging.INFO)

# ✅ Enable frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Request Schema
# ---------------------------
class ChatRequest(BaseModel):
    message: str
    provider: str = "ollama"
    session_id: str | None = None


# ---------------------------
# In-memory Session Store
# ---------------------------
sessions = {}

# ---------------------------
# Transcript Knowledge Base
# ---------------------------
transcripts = [
    {
        "episode": "Growth Fundamentals",
        "guest": "Lenny",
        "text": "Focus on retention over acquisition."
    },
    {
        "episode": "Scaling Products",
        "guest": "Lenny",
        "text": "Product market fit is critical before scaling."
    },
    {
        "episode": "User Research",
        "guest": "Lenny",
        "text": "Talk to users frequently."
    },
    {
        "episode": "Advanced Growth",
        "guest": "Lenny",
        "text": "Growth comes from understanding user behavior deeply."
    }
]

# ---------------------------
# Retrieval Logic (Improved)
# ---------------------------
def retrieve_context(query: str) -> List[dict]:
    results = []
    keywords = [w.lower() for w in query.split() if len(w) > 3]

    for t in transcripts:
        if any(word in t["text"].lower() for word in keywords):
            results.append(t)

    return results


# ---------------------------
# Health Endpoint
# ---------------------------
@app.get("/")
def home():
    return {"msg": "Running"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Lenny Growth Assistant",
        "timestamp": str(datetime.utcnow())
    }


# ---------------------------
# Session Creation
# ---------------------------
@app.post("/api/session")
def create_session():
    session_id = str(uuid.uuid4())
    sessions[session_id] = []
    return {"session_id": session_id}


# ---------------------------
# Chat Endpoint
# ---------------------------
@app.post("/api/chat")
def chat(req: ChatRequest):

    logging.info(f"Incoming query: {req.message}")

    # Create session if not exists
    if not req.session_id:
        req.session_id = str(uuid.uuid4())
        sessions[req.session_id] = []

    # Store user message
    sessions[req.session_id].append({
        "role": "user",
        "content": req.message
    })

    context = retrieve_context(req.message)

    # ---------------------------
    # No Context Handling
    # ---------------------------
    if not context:
        return {
            "session_id": req.session_id,
            "provider": req.provider,
            "answer": "I do not have sufficient information in Lenny's podcast transcripts to answer this."
        }

    # Format context
    formatted_context = "\n\n".join([
        f"[Episode: {c['episode']} | Guest: {c['guest']}]\n{c['text']}"
        for c in context
    ])

    # ---------------------------
    # Article Mode
    # ---------------------------
    if "article" in req.message.lower():

        article = f"""
# 🚀 The Hidden Truth About Growth Most Startups Ignore

## ⚡ The Real Growth Problem
Most teams chase acquisition. But according to Lenny’s insights, that’s a mistake.

## 🔍 What the Experts Say
{formatted_context}

## 🧠 Core Insight
Growth doesn’t come from hacks — it comes from understanding users deeply and delivering consistent value.

## 📈 The Growth Framework

- **Retention First** → Keep users before acquiring new ones  
- **PMF Validation** → Don’t scale without product-market fit  
- **User Conversations** → Talk to users every week  
- **Behavior Analysis** → Track how users interact  

## 🛠 Implementation Checklist

1. Track retention metrics weekly  
2. Interview 5 users every week  
3. Delay scaling until retention stabilizes  
4. Build feedback loops into product  

## 🎯 Final Takeaway
If users don’t stay, nothing else matters.
"""

        sessions[req.session_id].append({
            "role": "assistant",
            "content": article
        })

        return {
            "session_id": req.session_id,
            "provider": req.provider,
            "artifact": article
        }

    # ---------------------------
    # Normal Answer Mode
    # ---------------------------
    answer = f"""
### 📊 Context
{formatted_context}

### ✅ Answer
Focus on retention, validate product-market fit, and continuously engage with users.

### 📚 Sources
{formatted_context}
"""

    sessions[req.session_id].append({
        "role": "assistant",
        "content": answer
    })

    return {
        "session_id": req.session_id,
        "provider": req.provider,
        "answer": answer
    }
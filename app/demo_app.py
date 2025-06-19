from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# Ensure rag_chain is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag_chain.llm_chain import conversational_chain

# Load the chain once
_chain = conversational_chain()

def run_chatbot_query(query: str, history: list[str] = None) -> str:
    """
    Invoke the conversational chain with a user query and optional history.
    """
    try:
        input_data = {"question": query}
        if history:
            input_data["chat_history"] = history
        response = _chain.invoke(input_data)
        return response["answer"]
    except Exception as e:
        return f"Error: {str(e)}"

# FastAPI App
app = FastAPI()

# Optional: allow frontend access if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the RAG Chain API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/conversational")
def default_response():
    return {"response": run_chatbot_query("Hello, can you recommend me a credit card , i earn 10 lakh per year?")}

@app.get("/conversational/{query}")
def chatbot_with_query(query: str):
    return {"response": run_chatbot_query(query)}

@app.get("/conversational/{query}/history")
def chatbot_with_history(query: str, history: str = ""):
    history_list = history.split(",") if history else []
    return {"response": run_chatbot_query(query, history=history_list)}

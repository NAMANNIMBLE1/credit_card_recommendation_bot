# utilities/chroma_db.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # adding the root path manually for the utilities 

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from utilities.get_data import get_credit_cards




def format_card_to_document(card):
    """
    Converts a credit card dictionary to a LangChain Document.
    """
    content = f"""
    Name: {card['name']}
    Issuer: {card['issuer']}
    Joining Fee: {card['joining_fee']}
    Annual Fee: {card['annual_fee']}
    Reward Type: {card['reward_type']}
    Reward Rate: {card['reward_rate']}
    Eligibility: {card['eligibility']}
    Perks: {', '.join(card['special_perks'])}
    Apply Link: {card['apply_link']}
    """
    return Document(page_content=content.strip(), metadata={"name": card['name']})

def get_chroma_db(persist_directory: str = "chroma_db"):
    """
    Creates or loads a Chroma database with credit card data.
    
    Args:
        persist_directory (str): Directory to save/load Chroma DB.
    
    Returns:
        Chroma: The Chroma database retriever instance.
    """
    # Load data
    credit_cards = get_credit_cards()

    # Format to LangChain Documents
    documents = [format_card_to_document(card) for card in credit_cards]

    # Initialize embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create vectorstore (non-persistent by default, or enable persist=True)
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedding,
        persist_directory=persist_directory  # comment out if not persisting
    )

    return vectordb

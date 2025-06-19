# utilities/chroma_db.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # adding the root path manually for the utilities 
from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import  ChatGroq
from utilities.chroma_db import get_chroma_db_as_retriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnableSequence
from langchain.chains import (
    StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
)
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

def get_llm():
    """
    args: None
    returns: llm as ChatGroq object
    This function retrieves the LLM (Language Model) using the Groq API key from environment variables.
    It initializes a ChatGroq instance with the specified model and API key.
    The model used is "Llama3-8b-8192", which is a large language model.
    The function returns the initialized LLM instance.
    """
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        llm = ChatGroq(model="Deepseek-R1-Distill-Llama-70b", groq_api_key=groq_api_key , temperature=0)
        return llm
    except Exception as e:
        raise e


def get_retriever():
    """_summary_
    import the retriever function from utils and returns the retriever
    args: None
    returns : db as retriever (chromadb)
    """
    try:
        retriever = get_chroma_db_as_retriever()
        return retriever
    except Exception as e:
        raise e


# prompt template for the LLM chain
def get_prompt():
    """
    This function returns a prompt template for the credit card recommendation assistant.
    It is designed to guide the assistant in helping users in India choose the most suitable credit card based on their financial profile and lifestyle preferences.
    The prompt includes instructions for the assistant to collect user information step by step, recommend credit cards, and summarize the top recommendation.
    The prompt also includes a context variable that can be filled with relevant information about available credit cards.
    args: None
    returns: str
    A formatted string that serves as the prompt for the credit card recommendation assistant.
    """
    
    return """
    You are an expert and friendly credit card recommendation assistant trained specifically to help users in India choose the most suitable credit card based on their financial profile and lifestyle preferences.

    Always guide the user step by step in a conversational and helpful manner. Begin by warmly greeting them if this is their first message, and collect the following information **one at a time**, waiting for their input after each:

    1. **Monthly income**
    2. **Primary spending habits** (fuel, travel, groceries, dining, etc.)
    3. **Preferred benefits** (cashback, travel rewards, lounge access, etc.)
    4. **Existing credit cards** they currently use (optional)
    5. **Approximate credit score** (or accept "unknown")

    Once you collect all the necessary details:

    - **Filter and rank the top 3–5 Indian credit cards** based on the user's input and preferences using the most relevant information from the context and chat history.
    - For each recommended card, present the following:

    ---

    🔹 **Card Name**  
    🖼️ (Include card image if available via URL in context)  
    ✅ **Why this card is a good match** for the user's preferences  
    💸 **Reward Simulation**: Estimate how much the user could earn yearly (e.g., "You could earn ₹8,000/year cashback based on your profile")  
    💳 Annual/joining fee and whether it's worth it

    ---

    Finish by clearly summarizing **your top one card recommendation** with your reasoning.

    Important:
    - Be clear, concise, and engaging.
    - Only recommend cards that truly fit the user's profile.
    - If the user says something like “exit”, “quit”, or “bye”, end the conversation politely and warmly.

    Context:
    {context}

    User's message:
    {question}
    """
    


def conversational_chain():
    try:
        llm = get_llm() # getting the llm from the get_llm function
        retriever = get_retriever() # getting the retriever from the get_retriever function
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True,output_key="answer") # setting up the memory for the conversation

        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            
        )

        return chain

    except Exception as e:
        raise e




# if __name__ == "__main__":
#     print("Welcome to the Credit Card Assistant Chatbot!")
#     print("Type your queries below. Type 'exit' or 'quit' to end the conversation.\n")

#     chain = conversational_updated_chain()

#     while True:
#         user_input = input("You: ")

#         if user_input.lower() in ["exit", "quit"]:
#             print("Assistant: Thank you for using the assistant. Have a great day!")
#             break

#         try:
#             response = chain.invoke({"question": user_input})
#             print(f"Assistant: {response['answer']}\n")
#         except Exception as e:
#             print(f"An error occurred: {e}")

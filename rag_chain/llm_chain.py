import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv
load_dotenv()

from utilities.get_prompt import get_prompt_template
from utilities.chroma_db import get_chroma_db
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain import hub


def get_retriever():
    """
    Converts the VectorStore returned by ChromaDB into a retriever.
    """
    vectorstore = get_chroma_db()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    return retriever

def get_custom_prompt():
    """
    Returns a PromptTemplate using your imported template string.
    """
    prompt_template_str = get_prompt_template()
    return PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template_str
    )

def get_llm():
    import os
    api_key = os.getenv("HUGGINGFACEHUB_API_KEY")
    if not api_key:
        raise ValueError("HUGGINGFACEHUB_API_KEY not found in environment variables.")
    return HuggingFaceEndpoint(
        repo_id="google/flan-t5-large",  # or another accessible model
        max_new_tokens=100,
        do_sample=False,
        huggingfacehub_api_token=api_key
    )



def get_rag_chain():
    """
    Constructs the RAG chain using the retriever, prompt, and LLM.
    """
    retriever = get_retriever()
    prompt = get_custom_prompt()
    llm = get_llm()
    
    combs_doc_chain = create_stuff_documents_chain(llm , prompt)
    retriever_chain = create_retrieval_chain(retriever , combs_doc_chain)
    
    return retriever_chain


if __name__ == "__main__":
    
    chain = get_rag_chain()
    answer = chain.invoke({"input":"recommend me a card i earn 7000 rupees per month"})
    print(answer)

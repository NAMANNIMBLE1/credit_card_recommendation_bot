
# 💳 Credit Card Recommendation Bot

A smart AI-powered chatbot that provides personalized credit card recommendations based on user queries and preferences. Built for users seeking the best financial products, this bot leverages the latest in large language models (LLMs) and retrieval-augmented generation (RAG) technology.

# 🚀 Features

💡 Context-aware responses using the DeepSeek R1 LLM via ChatGroq

🔎 Retrieval-Augmented Generation (RAG) powered by ChromaDB

🧠 Embedded knowledge base using HuggingFace Embeddings

🕸️ Web interface using Flask, HTML, CSS, and JavaScript

⚡ API testing and prototyping with FastAPI


# 📚 Tech Stack


| Component        | Tech Used                   |
| ---------------- | --------------------------- |
| LLM              | DeepSeek R1 via ChatGroq    |
| Embeddings       | HuggingFace Transformers    |
| Vector Store     | ChromaDB                    |
| Backend          | Flask                       |
| Frontend         | HTML, CSS, JavaScript       |
| API Testing      | FastAPI                     |
| Memory & Context | Chat History with LangChain |



# 🧠 How It Works

User Query → Entered via the web interface.

Embedding & Retrieval → Query is converted into embeddings and matched with relevant documents using ChromaDB.

LLM Response Generation → Context + user query sent to DeepSeek R1 via ChatGroq for a final response.

Display → Flask renders the response on the web interface.
# Application preview

![App Screenshot](https://github.com/NAMANNIMBLE1/qa_chatbot/blob/main/pictures/screenshot_19062025_141814.jpg)
![App Screenshot](https://raw.githubusercontent.com/NAMANNIMBLE1/qa_chatbot/main/pictures/screenshot_19062025_141904.jpg)
![App Screenshot](https://raw.githubusercontent.com/NAMANNIMBLE1/qa_chatbot/main/pictures/screenshot_19062025_141945.jpg)
                                                                               


# Demo & UI interface

📹 [Watch Demo Video](https://raw.githubusercontent.com/NAMANNIMBLE1/qa_chatbot/main/video/demo_video.mp4)





# 📁 Folder Structure

```
credit-card-recommendation-bot/
├── .vscode/                    # VSCode settings
├── app/                        # Flask app module
│   ├── __init__.py
│   └── demo_app.py             # Main Flask app entry
├── data/
│   └── credit_cards.json       # Sample credit card dataset
├── prompt/
│   └── prompt.txt              # Custom prompt for LLM
├── rag_chain/                  # Retrieval-Augmented Generation logic
│   ├── __init__.py
│   ├── llm_chain.py            # LLM + Retriever Chain Logic
│   └── tempCodeRunnerFile.py   # Temporary/test file (can be removed)
├── static/
│   └── style.css               # Frontend styling
├── templates/
│   └── index.html              # Web interface layout
├── utilities/                  # Helper functions and modules
│   ├── __init__.py
│   ├── chroma_db.py            # ChromaDB initialization
│   ├── get_data.py             # Load and process credit card data
│   └── get_prompt.py           # Prompt loading logic
├── .env                        # Environment variables (API keys)
├── .gitignore                  # Git ignored files
├── app.py                      # Entry point (alternative or redirector)
├── pyproject.toml              # Project metadata/config (if using Poetry)
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies list
└── .python-version             # Python version spec (for pyenv)
```

# Setup & Installation

Install my-project using pip 

```bash
  pip install langchain 
  pip install langchain-groq
  pip install langchain-core 
  pip install langchain-huggingface 
  pip install langchain-chroma 
  pip install langchain-community
```
    
```bash
  pip install chromadb 
  pip install fastapi 
  pip install flask 
```

# 🧰 Installation
### 📦 Clone the Repository

```bash
git clone https://github.com/your-username/credit-card-recommendation-bot.git
cd credit-card-recommendation-bot
```

### 🧪 Create & Activate Environment

```bash 
   python -m venv env
   env\Scripts\activate   # On Windows
   source env/bin/activate  # on arch linux   
```

### 📥 Install Dependencies

Alternative , instead of downloading all packages manually do this 

```bash
  pip install -r requirements.txt 
```

### 🔐 Set Environment Variables

Create a .env file in the root directory and add:

```bash
  CHATGROQ_API_KEY=your_api_key_here
  HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

### 🚀 Run Flask App

```bash
   python app.py 
```

### ⚙️ (Optional) Run FastAPI for Testing

```bash 
   uvicorn api:app --reload
```
# 🛠️ Custom usecase & Future Improvements

## 🤖 Example Prompts

"What is the best credit card for online shopping?"

"Suggest a card with good travel rewards."

"I'm a student, which credit card suits me?"

## 🛠️ Future Improvements

better ui framework

custom Prompts chaining 

finetuning model based on real dataset

better history management 
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@NAMANNIMBLE1](https://github.com/NAMANNIMBLE1?tab=repositories)


## 🚀 About Me

Hi, I’m Naman Nimble — a passionate Data Scientist in the making and an enthusiastic learner of AI/ML technologies. Currently in my final year of B.Tech in Electronics and Communication Engineering at Netaji Subhas University of Technology (NSUT), I specialize in creating intelligent solutions that blend data, logic, and innovation.

This project showcases my interest in building smart recommendation systems using cutting-edge tools like LLMs, RAG architecture, and vector databases. By combining DeepSeek R1, ChromaDB, and Flask, I’ve built a chatbot that helps users find the best credit cards through natural conversation.

I’m continuously exploring:

Data Science & Machine Learning

Deep Learning and Generative AI

NLP & LLM Integration


📫 Let’s connect:
📧 Email: naman.nimble.ug21@nsut.ac.in


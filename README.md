# 💻 RAG Intelligent Agent
---
This project provides a modular Streamlit app built with **LangChain**, **FAISS**, **Ollama**, **Wikipedia**, and **Arxiv tools** to answer questions about LangFlow using retrieval-augmented generation (RAG) + tool-calling agents.


## Requirements
- Python 3.12+
- Local Ollama server with Llama3 model
- GPU-enabled environment recommended for faster response

## Features
- 🔎 **Wikipedia + Arxiv Search**
- 📚 **FAISS Vector Retrieval** built from LangFlow documentation
- 🤖 **Agent with Tool-Calling** (OpenAI-style)
- 💬 **Interactive Streamlit UI**
- ⚡ **Local Llama 3 via Ollama**
- 🧩 **Modular architecture** for easy extension  

## Technologies Used:
- Streamlit, Python, VectorDB (FAISS)
- Tools used: Arxiv, Wikipedia
- Models used: Chat model -> Llama3 
- Prompt: hwchase17/openai-functions-agen

## Project Structure

```bash
Langchain_basic/
├── db/faiss_db          # For storing and loading the vector database
├── app.py               # Streamlit app for user
├── modules/
│ ├── agent.py
│ ├── tool_setup.py
│ ├── vectorstore.py
│ └── config.py
├── README.md
├── agents.ipynb            # simple rag implementation with jupyter notebook
└─ requirements.txt      # Python dependencies
```

## 🧠 How It Works 
- Vectorstore Builder scrapes Langflow docs and builds a FAISS DB
- Retriever Tool allows agents to search the vector DB
- Wikipedia & Arxiv Tools enable external lookups
- ChatOllama Agent uses OpenAI-style tool-calling to decide which tool to query
- Streamlit App lets users enter questions and streams agent responses

## 📌 Notes
- The vector DB is automatically built on first run
- You can extend tools by modifying modules/tool_setup.py
- You can switch to any other Ollama model via config.py


## Installation

## 🛠 Installation

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Multi_Search_Agent_RAG.git
cd searchrag
```
### 2. Requirements.txt
```bash
langchain
langchain_community
langchain-core
langchain-classic
langchainhub
ipykernel
streamlit
faiss-cpu
arxiv
wikipedia
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit app
```bash
streamlit run app.py

```
Open in your browser:
```
👉 http://localhost:8501/
👉 Enter your queries and then click on submit button
👉 Based on the query, it will use the tools to generate the answer
```

## Demo
https://github.com/user-attachments/assets/40931b6d-afeb-4d61-be68-32ee20246c3f

## License
[MIT](https://choosealicense.com/licenses/mit/)



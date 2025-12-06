import streamlit as st
from modules.tool_setup import initialize_tools
from modules.agent import build_agent
from modules.vectorstore import build_vectorstore, load_vectorstore
from modules.config import VECTOR_DB_PATH
import os

st.set_page_config(page_title="LangFlow Agent", layout="wide")

st.title("🔍 RAG Intelligent Agent")
st.caption("Powered by LangChain, FAISS, Ollama, Wikipedia, and Arxiv")

# --- Initialization ---
if not os.path.exists(VECTOR_DB_PATH):
    st.write("🔨 Building vector database...")
    build_vectorstore()

tools = initialize_tools()
agent_executor = build_agent(tools)

# --- User Input ---
query = st.text_input("Ask anything about LangFlow:")

if st.button("Run Query") and query.strip():
    st.write("### Response:")
    with st.spinner("Thinking..."):

        # Stream response
        response_stream = agent_executor.stream({"input": query})
        for chunk in response_stream:
            if "output" in chunk:
                st.write(chunk["output"])

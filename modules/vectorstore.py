from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from modules.config import (
    CHUNK_SIZE, CHUNK_OVERLAP, OLLAMA_MODEL, VECTOR_DB_PATH, LANGFLOW_URL,
)
import os

def build_vectorstore():
    loader = WebBaseLoader(LANGFLOW_URL)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    documents = splitter.split_documents(docs)

    vectordb = FAISS.from_documents(
        documents, OllamaEmbeddings(model=OLLAMA_MODEL)
    )

    os.makedirs(os.path.dirname(VECTOR_DB_PATH), exist_ok=True)
    vectordb.save_local(VECTOR_DB_PATH)

    return vectordb


def load_vectorstore():
    return FAISS.load_local(
        VECTOR_DB_PATH,
        OllamaEmbeddings(model=OLLAMA_MODEL),
        allow_dangerous_deserialization=True
    )

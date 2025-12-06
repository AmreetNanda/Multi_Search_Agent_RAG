from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain_classic.tools.retriever import create_retriever_tool
from modules.vectorstore import load_vectorstore
from modules.config import (
    WIKI_TOP_K, ARXIV_TOP_K
)

def initialize_tools():
    # Wikipedia
    wiki = WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(
            top_k_results=WIKI_TOP_K,
            doc_content_chars_max=200
        )
    )

    # Arxiv
    arxiv = ArxivQueryRun(
        api_wrapper=ArxivAPIWrapper(
            top_k_results=ARXIV_TOP_K,
            doc_content_chars_max=200
        )
    )

    # Retriever (FAISS)
    vectordb = load_vectorstore()
    retriever = vectordb.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "langflow_search",
        "Search for information about Langflow. For any questions about Langflow, use this tool."
    )

    return [wiki, arxiv, retriever_tool]

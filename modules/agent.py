# modules/agent.py

from langchain_community.chat_models import ChatOllama
from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_classic import hub
from modules.config import OLLAMA_MODEL

def build_agent(tools):
    llm = ChatOllama(model=OLLAMA_MODEL, temperature=0)

    prompt = hub.pull("hwchase17/openai-functions-agent")

    agent = create_openai_tools_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        stream_runnable=True
    )

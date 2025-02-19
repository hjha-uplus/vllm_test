from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI


inference_server_url = "http://localhost:8000/v1"

llm = ChatOpenAI(
    model="Qwen/Qwen2-VL-2B-Instruct",
    openai_api_key="",
    openai_api_base=inference_server_url,
    max_tokens=5,
    temperature=0,
)

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to Italian."
    ),
    HumanMessage(
        content="Translate the following sentence from English to Italian: I love programming."
    ),
]
print(llm.invoke(messages))
print(llm.batch([messages] * 3))
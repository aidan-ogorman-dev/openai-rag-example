from langserve import RemoteRunnable
from langchain_core.messages import HumanMessage, AIMessage

remote_chain = RemoteRunnable("http://localhost:8000/chat/")
result = remote_chain.invoke(
    {"input": "What is Task Decomposition?"},
    config={
        "configurable": {"session_id": "abc123"}
    },  # constructs a key "abc123" in `store`.
)["answer"]

print(result)

result2 = remote_chain.invoke(
    {"input": "What are common ways of doing it?"},
    config={"configurable": {"session_id": "abc123"}},
)["answer"]

print(result2)
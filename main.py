#import relevant functionality
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os
from langchain_groq import ChatGroq


os.environ["TAVILY_API_KEY"] = "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"

os.environ["GROQ_API_KEY"] = "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"


# Create the agent
memory = MemorySaver()
model = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.8,
    max_tokens=2048
)

print("Tavily was instatiated")

search = TavilySearchResults(
    max_results=4,
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)


tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)


# use the agent
config = {"configurable": {"thread_id": "abc12345"}}
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="HI, this is Jessi!, and I live in NY")]}, config
) :
    print(chunk)
    print("---")
    
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="Whats the weather where I live?")]}, config
) :
    print(chunk)
    print("---")
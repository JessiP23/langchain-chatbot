#import relevant functionality
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent


# Create the agent
memory = MemorySaver()
model = ChatAnthropic(model_name="claude-3-sonnet-20240229")
search = TavilySearchResults(max_results=3)
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
import os
from http.client import responses

from dotenv import load_dotenv # used to safely load API keys or .env file
from langchain.chains.summarize.map_reduce_prompt import prompt_template

from langchain_core.messages import HumanMessage, AIMessage # represents chat messages user input to model response
from langchain_core.output_parsers import StrOutputParser # converts the model output into a plain string
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # used to build chat prompts dynamically , create the reusable prompts and stores conversation memory
from langchain_google_genai import ChatGoogleGenerativeAI # connects  to the Google Gemini with langchain and this is llm (brain) of the chatbot
from pydantic_core.core_schema import  model_field # low level schema handling
from langchain.tools import tool # converts a python function into AI-callable tool
from langchain.agents import create_openai_tools_agent, AgentExecutor # creates an agent and runs the agent
from todoist_api_python.api import TodoistAPI # connects your app to Todoist


load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

@tool
def add_task(task, description=None):
    """Add a new task to the user's task list. Use this when the user wants to add or create a task """
    todoist.add_task(content=task,
                     description=description)

@tool
def show_tasks():
    """show all tasks from Todoist. Use this tool when the user wants to  see their tasks.."""
    results_paginator = todoist.get_tasks()
    tasks = []
    for task_list in results_paginator:
        for task in task_list:
            tasks.append(task.content)
    return tasks


tools = [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = """You r a helpful assistant.
You wil help the user add tasks.
You will help the user show existing tasks.
"""


prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history")
])

# chain = prompt | llm |StrOutputParser()

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


# response = chain.invoke({"input":user_input})

history = []
while True:
    user_input = input("You: ")
    response = agent_executor.invoke({"input": user_input,"history": history})
    print(response['output'])
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response['output']))
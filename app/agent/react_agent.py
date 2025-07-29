from app.tools.react_agent_tools import get_word_length
import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv


class MyReactAgent:
    """
    A ReAct agent that uses Gemini, has memory, and can be equipped with custom tools.
    """
    def __init__(self, verbose=True):
        """
        Initializes the agent, its tools, the LLM, and the executor.
        Args:
            verbose (bool): Whether to print the agent's thought process.
        """
        # 0. Set up the environment variables.
        load_dotenv('/app/.env')
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        print(GOOGLE_API_KEY)

        # 1. Define the tools the agent will have access to.
        self.tools = [get_word_length]

        # 2. Initialize the LLM. We use Gemini Pro for this example.
        # Temperature is set to 0 for more deterministic outputs.
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

        # 3. Pull the ReAct prompt template from LangChain Hub.
        # This prompt is specifically designed to work with ReAct agents.
        self.prompt = hub.pull("hwchase17/react")

        # 4. Create the ReAct agent by combining the LLM, tools, and prompt.
        self.agent = create_react_agent(self.llm, self.tools, self.prompt)

        # 5. Set up memory to retain conversation history.
        # The `memory_key` must match the one in the prompt.
        self.memory = ConversationBufferMemory(memory_key="chat_history")

        # 6. Create the AgentExecutor. This is the runtime for the agent.
        # It orchestrates the calls to the LLM and tools.
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=verbose,
            memory=self.memory,
            handle_parsing_errors=True, # Handles errors if the LLM output is not parsable
        )

    def invoke(self, user_input: str) -> str:
        """
        Invokes the agent with a user query and returns the response.

        Args:
            user_input (str): The query or message from the user.

        Returns:
            str: The agent's response.
        """
        response = self.agent_executor.invoke({"input": user_input})
        return response.get("output", "Sorry, I encountered an error.")
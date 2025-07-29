# agent service logic basically agent logic part.
from typing import Optional
from app.agent.react_agent import MyReactAgent
import json

class AgentService:
    @classmethod
    def process_string(cls, input_string: str) -> str:
        if not input_string or input_string.strip() == "":
            return "Please provide a valid input string."
        
        react_agent = MyReactAgent()
        agent_response = react_agent.invoke(input_string.strip())
        print(agent_response)
        return json.dumps(agent_response)
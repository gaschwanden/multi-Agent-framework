from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create assistant agent
assistant = AssistantAgent(name="assistant", llm_config={
                           "config_list": config_list})

# Create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "SalesAgent"})

# Start the conversation


user_proxy.initiate_chat(
    assistant, message= "We are a company with four verticals that operates as marketplaces within the automotive, real estate, finance and general marketplaces sector. We have separate teams with separate technologies creating silos, higher cost and people not being able to work with each other. Can you help me to figure out how to consolidate technologies and bring people together to share data and ways of working.")
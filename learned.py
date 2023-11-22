from autogen import UserProxyAgent, config_list_from_json
from autogen.agentchat.contrib.teachable_agent import TeachableAgent

# Load LLM inference endpoints from an env variable or a file
filter_dict = {"model": ["gpt-4"]}  # GPT-3.5 is less reliable than GPT-4 at learning from user feedback.
config_list = [ 
    {
        # 'model': 'gpt-4',
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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'
    }
]
llm_config={"config_list": config_list, "request_timeout": 120}

teachable_agent = TeachableAgent(
    name="teachableagent",
    llm_config=llm_config,
    teach_config={
        "reset_db": False,  # Use True to force-reset the memo DB, and False to use an existing DB.
        "path_to_db_dir": "./tmp/interactive/teachable_agent_db"  # Can be any path.
    }
)

user = UserProxyAgent("user", human_input_mode="ALWAYS")

# This function will return once the user types 'exit'.
teachable_agent.initiate_chat(user, message="Hi, I'm a teachable user assistant! What's on your mind?")

# Before closing the app, let the teachable agent store things that should be learned from this chat.
teachable_agent.learn_from_user_feedback()
teachable_agent.close_db()
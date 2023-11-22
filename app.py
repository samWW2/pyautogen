import autogen

config_list = [ 
    {
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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'
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=2,
    is_termination_msg=lambda x: x.get("content", "").endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE to quit or CONTINUE to keep going."""
)

task = input("Please enter a task: ")

user_proxy.initiate_chat(
    assistant,
    message=task
)
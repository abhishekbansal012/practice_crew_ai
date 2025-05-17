import os
from autogen import AssistantAgent
from tools import reflection_message

# Get API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# LLM configuration
llm_config = {
    "config_list": [
        {
            "model": "gpt-4-turbo",
            "api_key": openai_api_key
        }
    ]
}

# Writer Agent
writer = AssistantAgent(
    name="Writer",
    system_message=(
        "You are a writer. You write engaging and concise blogposts (with title) "
        "on given topics. You must polish your writing based on the feedback you "
        "receive and give a refined version. Only return your final work without additional comments."
    ),
    llm_config=llm_config,
)

# Critic Agent
critic = AssistantAgent(
    name="Critic",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=llm_config,
    system_message="You are a critic. You review the work of the writer and provide constructive feedback.",
)

# Reviewers
SEO_reviewer = AssistantAgent(
    name="SEOReviewer",
    llm_config=llm_config,
    system_message="You are an SEO reviewer. Optimize content for search engines in 3 concise bullet points."
)

legal_reviewer = AssistantAgent(
    name="LegalReviewer",
    llm_config=llm_config,
    system_message="You are a legal reviewer. Ensure content is legally compliant. Respond in 3 concise bullet points."
)

ethics_reviewer = AssistantAgent(
    name="EthicsReviewer",
    llm_config=llm_config,
    system_message="You are an ethics reviewer. Ensure ethical soundness. Respond in 3 concise bullet points."
)

meta_reviewer = AssistantAgent(
    name="MetaReviewer",
    llm_config=llm_config,
    system_message="You are a meta reviewer. Aggregate other reviewers’ feedback and suggest final improvements."
)

# Register nested review chats
review_chats = [
    {
        "recipient": SEO_reviewer,
        "message": lambda recipient, messages, sender, config: reflection_message(recipient, sender),
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": (
                "Return review into a JSON object only: "
                "{'Reviewer': '', 'Review': ''}"
            )
        },
        "max_turns": 1
    },
    {
        "recipient": legal_reviewer,
        "message": lambda recipient, messages, sender, config: reflection_message(recipient, sender),
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": (
                "Return review into a JSON object only: "
                "{'Reviewer': '', 'Review': ''}"
            )
        },
        "max_turns": 1
    },
    {
        "recipient": ethics_reviewer,
        "message": lambda recipient, messages, sender, config: reflection_message(recipient, sender),
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": (
                "Return review into a JSON object only: "
                "{'Reviewer': '', 'Review': ''}"
            )
        },
        "max_turns": 1
    },
    {
        "recipient": meta_reviewer,
        "message": lambda recipient, messages, sender, config: "Aggregate feedback from all reviewers and give final suggestions on the writing.",
        "max_turns": 1
    }
]

# Register nested review flow with critic
critic.register_nested_chats(
    review_chats,
    trigger=writer,
)

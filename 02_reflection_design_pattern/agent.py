import os
from autogen import AssistantAgent

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

# Initial task
task = "Write a blog post about the benefits of remote work."

# Writer agent
writer = AssistantAgent(
    name="Writer",
    system_message=(
        "You are a writer. You write engaging and concise blogposts (with title) "
        "on given topics. You must polish your writing based on the feedback you "
        "receive and give a refined version. Only return your final work without additional comments."
    ),
    llm_config=llm_config,
)

# Critic agent
critic = AssistantAgent(
    name="Critic",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=llm_config,
    system_message="You are a critic. You review the work of "
                   "the writer and provide constructive "
                   "feedback to help improve the quality of the content.",
)

# Reviewers
SEO_reviewer = AssistantAgent(
    name="SEOReviewer",
    llm_config=llm_config,
    system_message="You are an SEO reviewer, known for "
                   "your ability to optimize content for search engines, "
                   "ensuring that it ranks well and attracts organic traffic. " 
                   "Make sure your suggestion is concise (within 3 bullet points), "
                   "concrete and to the point. "
                   "Begin the review by stating your role.",
)

legal_reviewer = AssistantAgent(
    name="LegalReviewer",
    llm_config=llm_config,
    system_message="You are a legal reviewer, known for "
                   "your ability to ensure that content is legally compliant "
                   "and free from any potential legal issues. "
                   "Make sure your suggestion is concise (within 3 bullet points), "
                   "concrete and to the point. "
                   "Begin the review by stating your role.",
)

ethics_reviewer = AssistantAgent(
    name="EthicsReviewer",
    llm_config=llm_config,
    system_message="You are an ethics reviewer, known for "
                   "your ability to ensure that content is ethically sound "
                   "and free from any potential ethical issues. " 
                   "Make sure your suggestion is concise (within 3 bullet points), "
                   "concrete and to the point. "
                   "Begin the review by stating your role.",
)

meta_reviewer = AssistantAgent(
    name="MetaReviewer",
    llm_config=llm_config,
    system_message="You are a meta reviewer. You aggregate and review "
                   "the work of other reviewers and give a final suggestion on the content.",
)

# Helper function for review message
def reflection_message(recipient, sender):
    return f'''Review the following content:\n\n{recipient.chat_messages_for_summary(sender)[-1]['content']}'''


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


critic.register_nested_chats(
    review_chats,
    trigger=writer,
)

# Start the review interaction
res = critic.initiate_chat(
    recipient=writer,
    message=task,
    max_turns=2,
    summary_method="last_msg"
)

print(res.summary)

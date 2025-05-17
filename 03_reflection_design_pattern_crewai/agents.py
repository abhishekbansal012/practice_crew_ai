from crewai import Agent

writer = Agent(
    role="Writer",
    goal="Create an engaging blog post with a title on the given topic.",
    backstory="A creative writer skilled at crafting informative and engaging articles.",
    allow_delegation=False
)

critic = Agent(
    role="Critic",
    goal="Critically review the blog post and get input from domain-specific reviewers.",
    backstory="An experienced editor who leverages expert reviewers to improve content quality.",
    allow_delegation=True
)

seo_reviewer = Agent(
    role="SEO Reviewer",
    goal="Ensure the content is optimized for search engines with 3 bullet point suggestions.",
    backstory="An SEO specialist who helps articles rank high on Google.",
    allow_delegation=False
)

legal_reviewer = Agent(
    role="Legal Reviewer",
    goal="Ensure the article does not include legally problematic content with 3-point feedback.",
    backstory="A legal expert that ensures compliance and avoids legal pitfalls.",
    allow_delegation=False
)

ethics_reviewer = Agent(
    role="Ethics Reviewer",
    goal="Ensure the content is ethically appropriate and sensitive.",
    backstory="An ethics expert ensuring that articles are morally sound and inclusive.",
    allow_delegation=False
)

meta_reviewer = Agent(
    role="Meta Reviewer",
    goal="Aggregate feedback from other reviewers and suggest final changes.",
    backstory="A senior editor who compiles expert feedback into clear improvement suggestions.",
    allow_delegation=False
)

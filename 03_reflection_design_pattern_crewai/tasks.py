from crewai import Task

def create_tasks(topic, writer, critic, seo, legal, ethics, meta):
    write_blog = Task(
        description=f"Write a blog post about: {topic}",
        agent=writer,
        expected_output="A complete blog post with a title.",
        output_file="blog_post.md"
    )

    critic_review = Task(
        description="Review the written blog post and delegate to SEO, Legal, and Ethics reviewers.",
        agent=critic,
        expected_output="Constructive feedback from all reviewers.",
        context=[write_blog]
    )

    seo_task = Task(
        description="Review the blog post for SEO issues. Provide 3 bullet points.",
        agent=seo,
        expected_output="{'Reviewer': 'SEO', 'Review': '...'}",
        context=[write_blog]
    )

    legal_task = Task(
        description="Review the blog post for legal issues. Provide 3 bullet points.",
        agent=legal,
        expected_output="{'Reviewer': 'Legal', 'Review': '...'}",
        context=[write_blog]
    )

    ethics_task = Task(
        description="Review the blog post for ethical issues. Provide 3 bullet points.",
        agent=ethics,
        expected_output="{'Reviewer': 'Ethics', 'Review': '...'}",
        context=[write_blog]
    )

    meta_review = Task(
        description="Aggregate all reviewer feedback and provide final suggestions for improvement.",
        agent=meta,
        expected_output="Final consolidated feedback for improvement.",
        context=[seo_task, legal_task, ethics_task]
    )

    return [write_blog, critic_review, seo_task, legal_task, ethics_task, meta_review]

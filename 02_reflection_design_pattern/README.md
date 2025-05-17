# Blog post writer and feedback system
You have a writer agent that generates a blog post, and multiple reviewer agents that critique the post. The critic agent acts as the orchestrator, sending the writer’s output to the reviewers and receiving their feedback.

👥 Agents Involved
Agent	Role
Writer	Generates the blog post.
Critic	Coordinates reviews and provides feedback to the writer.
SEOReviewer	Reviews the content for SEO optimization.
LegalReviewer	Checks the content for legal compliance.
EthicsReviewer	Ensures ethical integrity of the content.
MetaReviewer	Consolidates feedback from all reviewers and gives final suggestion.

## Installation steps

### Step 1
conda create -p venv python==3.10 -y
### Step 2 
conda activate <> as per logs
### Step 3
pip install -r requirements.txt

## Usage
python crew.py 
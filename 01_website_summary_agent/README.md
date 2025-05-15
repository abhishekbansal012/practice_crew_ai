# Article Summary Agent
This Agent uses OpenAI LLM Agent. Please provide current OPENAI_API_KEY values in env variables. 

## 🚀 Features

- Scrapes text content from any Medium article URL.
- Uses an LLM(OpenAI) agent to summarize the article in 5–7 bullet points.
- Saves the summary in a `summary.md` file.
- Modular structure with `agents`, `tasks`, `tools`, and `crew`.

## Installation steps

### Step 1
conda create -p venv python==3.10 -y 
### Step 2 
conda activate
### Step 3
pip install -r requirements.txt

## Usage
python crew.py 
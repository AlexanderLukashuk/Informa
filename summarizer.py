# summarizer.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

messages = [
    {"role": "system", "content": "Please provide a concise summary of the following article:\n\n{content}\n\nSummary:"},
]


def summarize_article(content):
    response = openai.Completion.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    return response.choices[0].message.content.strip()

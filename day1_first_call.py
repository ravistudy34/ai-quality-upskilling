import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

response = client.messages.create(
    model ="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {"role": "user" , "content": "Exlain what a hallucination is in an LLM in 2 sentences , using a QA testing analogy."}
    ]
)
print(response.content[0].text)
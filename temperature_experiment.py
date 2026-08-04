import os
import anthropic
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
prompt = "Suggest a name for a new QA automation tool"

for temp in [0.0, 0.5, 1.0]:
    print(f"\n-- Temperature: {temp} ---")
    for i in range(3):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=150,
            temperature=temp,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        print(f"Run {i+1}: {response.content[0].text.strip()}")

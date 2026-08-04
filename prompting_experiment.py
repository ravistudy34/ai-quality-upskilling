import os
import anthropic
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# 1.Zero shot
zero_shot = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Classify this bug report severity: 'Login button is 2px off-center on the signup page.' Only respond with the severity level, no explanation."}
    ]
)
print("---Zero Shot ----")
print(zero_shot.content[0].text)


#2 Few-shot
few_shot_prompt = """Classify the bug severity as Critical , High , Medium or Low.Examples:
Bug : " App crashes when user taps checkout button"
severity : Critical

Bug: "typo in footer copywright year"
severity : Low

Now classigy this Bug:
Bug: "Login button is 2px off-center on the signup page."
Severity : 
Only resond with the severity level, no explanation."""

few_Shot = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=40,
    messages=[
        {"role": "user", "content": few_shot_prompt}
    ]
)
print("\n---Few Shot----")
print(few_Shot.content[0].text)

# 3. System prompt
system_prompt =  client.messages.create(
    model="claude-sonnet-4-6",  
    max_tokens=40,
    system = "you are strict QA triage bot. Respond with ONLY one word: Critical, High, Medium or Low. No explanation.",
    messages=[
        {"role": "user", "content": "Classify this bug report severity: 'Login button is 2px off-center on the signup page.'"}
    ]
)
print("\n---System Prompt----")
print(system_prompt.content[0].text)


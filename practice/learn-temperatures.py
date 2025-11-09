import os
from openai import OpenAI

"""
A simple example to demonstrate that higher temperature gives more creativity and lower temperature
keeps creativity lower.

Expected temperature to be at most 2, else OpenAI module will throw a 400 with bad request error
"""
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

# Create a detailed prompt
prompt = """
Create a product description for SonicPro headphones with key features that include Active noise cancellation (ANC), 40-hour battery life, Foldable design
"""

response = client.chat.completions.create(
    model="meta-llama/llama-3.3-70b-instruct:free",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    temperature=1
)

print(response.choices[0].message.content)

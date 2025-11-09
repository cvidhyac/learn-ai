import os

from openai import OpenAI
"""
There are two ways an LLM learns:
- One shot prompting: Send a given question to LLM without any examples
- Few shot prompting: Send an example to LLM along with prompt

When given examples and/or step by step prompting there are many math yardsticks that prove
that the output received from the LLM becomes more deterministic.
"""

# define a multi-line prompt to classify sentiment

prompt = """ Classify the customer sentiment for the reviews from an online store"
1. Unbelievably good! -> 5
2. Shoes fell apart on the second use. -> 1
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!
"""

client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENAI_API_KEY"))

# create a request to chat completions endpoint

response = client.chat.completions.create(model="minimax/minimax-m2:free",
                                          messages=[{"role": "user", "content": prompt}],
                                          max_completion_tokens=400, temperature=1)
print(response.choices[0].message.content)

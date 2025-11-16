import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
"""
There are two ways an LLM learns:
- One shot prompting: Send a given question to LLM without any examples
- Few shot prompting: Send an example to LLM along with prompt

When given examples and/or step by step prompting there are many math yardsticks that prove
that the output received from the LLM becomes more deterministic.

As part of this learning, i wrote two examples, one that uses few-shot prompting, then another
with fixed formatting.
"""


"""
Example 1:
Define a multi-line prompt to give a couple of examples against each prompt
We specify arrows and aren't very particular on formatting.
"""


def basic_few_shot_prompting(client: OpenAI) -> None:
    prompt = """ Classify the customer sentiment for the reviews from an online store"
    1. Unbelievably good! -> 5
    2. Shoes fell apart on the second use. -> 1
    3. The shoes look nice, but they aren't very comfortable.
    4. Can't wait to show them off!
    """
    execute_prompt(client, prompt)


"""
Here we add examples similar to previous one, however give LLM an indication to reduce verbosity
and stick format by indicating we only need `=` and the result.

The result is that LLM picks up the cue and provides the response what we need with precise instructions
"""


def improved_few_shot_prompting(client: OpenAI) -> None:
    prompt = """ Classify sentiment as 1-5 (negative to positive)"
    1. Unbelievably good! = 5
    2. Shoes fell apart on the second use. = 1
    3. The shoes look nice, but they aren't very comfortable. =
    4. Can't wait to show them off! =
    5. The quality was not what i expected =
    """
    execute_prompt(client, prompt)


"""
Utility method that defines a pre-defined model for this example
We limit to 250 tokens here and keep a static temperature of 1, since intent is to understand how
sentiment classification is interpreted by LLM
"""


def execute_prompt(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=300, temperature=1
    )
    print(response.choices[0].message.content)
    print("---------------end prompt execution ------------------")


if __name__ == "__main__":
    openai_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENAI_API_KEY"))
    basic_few_shot_prompting(openai_client)
    improved_few_shot_prompting(openai_client)

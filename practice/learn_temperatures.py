import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

"""
A simple example to demonstrate that higher temperature gives more creativity and lower temperature
keeps creativity lower.

Expected temperature to be at most 2, else OpenAI module will throw a 400 with bad request error
"""
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENAI_API_KEY"))
prompt = """
Create a product description for SonicPro headphones with key features that include Active noise cancellation (ANC), 40-hour battery life, Foldable design
"""


def test_different_temperatures(temps: list) -> None:
    for value in temps:
        if value > 2:
            print("Anything over 2 is an invalid temperature range, this will be skipped")
            continue
        execute_prompt(value)


"""
Execute a prompt with a given temperature
"""


def execute_prompt(temperature_value: float) -> None:
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        # Experiment with max_completion_tokens and temperature settings
        max_completion_tokens=100,
        temperature=temperature_value,
    )
    print(response.choices[0].message.content)
    print("-------end prompt execution---------")


if __name__ == "__main__":
    test_different_temperatures([0, 0.8, 1.9])

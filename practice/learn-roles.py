"""
See notes/building-conversations.md for a detailed explanation on llm roles.
"""
import os

from openai import OpenAI


def execute_prompt(prompt):
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="ibm-granite/granite-4.0-h-micro",
        max_completion_tokens=250,
        temperature=1,
        messages=[{
            "role": "system",
            "content": "You are a python tutor that speaks concisely"
        },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(response.choices[0].message.content)

def ask_python_question():
    prompt = input("Enter a python question:")
    execute_prompt(prompt)


if __name__ == '__main__':
    ask_python_question()
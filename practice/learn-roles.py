"""
See notes/building-conversations.md for a detailed explanation on llm roles.
"""
import os

from openai import OpenAI

"""
Execute a prompt with given user and system role messages
"""
def execute_prompt(user_prompt: str, system_prompt: str):
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="ibm-granite/granite-4.0-h-micro",
        max_completion_tokens=250,
        temperature=1,
        messages=[{
            "role": "system",
            "content": system_prompt
        },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    print(response.choices[0].message.content)

"""
Example using standard prompt without guardrails
"""
def ask_python_question():
    standard_sys_prompt = "You are a python tutor that speaks concisely"
    prompt = input("Enter a python question:")
    execute_prompt(prompt, standard_sys_prompt)

"""
Example applying a stronger guardrail in system message to prevent LLM misuse
"""
def ask_question():
    sys_prompt_with_guardrails = f"""You are a python tutor that speaks concisely. If you are asked any questions not related to python
               coding or concepts, please answer 'Apologies, to focus on python, I am not allowed to answer other topics')
               """
    prompt = input("Enter another python question:")
    execute_prompt(prompt, sys_prompt_with_guardrails)


if __name__ == '__main__':
    ask_python_question()
    ask_question()

"""
See notes/building-conversations.md for a detailed explanation on llm roles.
"""
import os

from openai import OpenAI

"""
Execute a prompt with given user and system role messages
"""
def execute_prompt(input_msg: list[dict[str, str]]):
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="ibm-granite/granite-4.0-h-micro",
        max_completion_tokens=250,
        temperature=1,
        messages=input_msg
    )
    print(response.choices[0].message.content)
    print("------- end prompt execution -------------")

"""
Example using standard prompt without guardrails
"""
def ask_python_question():
    standard_sys_prompt = "You are a python tutor that speaks concisely"
    prompt = input("Enter a python question:")
    msg = [{
        "role": "system",
        "content": standard_sys_prompt
    },
        {
            "role": "user",
            "content": prompt
        }
    ]
    execute_prompt(msg)

"""
Example applying a stronger guardrail in system message to prevent LLM misuse
"""
def ask_question():
    sys_prompt_with_guardrails = f"""You are a python tutor that speaks concisely. If you are asked any questions not related to python
               coding or concepts, please answer 'Apologies, to focus on python, I am not allowed to answer other topics')
               """
    prompt = input("Enter another python question:")

    msg = [{
        "role": "system",
        "content": sys_prompt_with_guardrails
    },
        {
            "role": "user",
            "content": prompt
        }
    ]

    execute_prompt(msg)

"""
Example with system, user and assistant messages
"""
def applying_user_assistant_examples():
    system_message = f"""You are a helpful geography tutor that generates concise summaries of 100 words for different 
    countries. When asked about topics unreleated to geography respond with - 'I am not allowed to answer'"""
    msg = [
        { "role": "system", "content": system_message},
        { "role": "user", "content": "What is the weather today?"},
        { "role": "assistant", "content": "I am not allowed to answer"},
        { "role": "user", "content": "Give me an overview of France"},
        {"role": "assistant", "content": "France is a beautiful country. Paris is the capital of france"},
        {"role": "user", "content": "Give me a summary of Spain's history"}
    ]
    execute_prompt(msg)

if __name__ == '__main__':
    ask_python_question()
    ask_question()
    applying_user_assistant_examples()
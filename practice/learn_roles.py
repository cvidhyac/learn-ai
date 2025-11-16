"""
See notes/building-conversations.md for a detailed explanation on llm roles.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

# Load environment variables from .env file
load_dotenv()

"""
Execute a prompt with given user and system role messages
"""


def execute_prompt(input_msg: list[ChatCompletionMessageParam]):
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="ibm-granite/granite-4.0-h-micro", max_completion_tokens=250, temperature=1, messages=input_msg
    )
    print(response.choices[0].message.content)
    print("------- end prompt execution -------------")


def system_message(content: str) -> ChatCompletionSystemMessageParam:
    return {"role": "system", "content": content}  # type: ignore[return-value]


def user_message(content: str) -> ChatCompletionUserMessageParam:
    return {"role": "user", "content": content}  # type: ignore[return-value]


def assistant_message(content: str) -> ChatCompletionAssistantMessageParam:
    return {"role": "assistant", "content": content}  # type: ignore[return-value]


"""
Example using standard prompt without guardrails
"""


def ask_python_question():
    standard_sys_prompt = "You are a python tutor that speaks concisely"
    prompt = input("Enter a python question:")
    msg: list[ChatCompletionMessageParam] = [system_message(standard_sys_prompt), user_message(prompt)]
    execute_prompt(msg)


"""
Example applying a stronger guardrail in system message to prevent LLM misuse
"""


def ask_question():
    sys_prompt_with_guardrails = """You are a python tutor that speaks concisely. If you are asked any questions not related to python
               coding or concepts, please answer 'Apologies, to focus on python, I am not allowed to answer other topics')
               """
    prompt = input("Enter another python question:")

    msg: list[ChatCompletionMessageParam] = [system_message(sys_prompt_with_guardrails), user_message(prompt)]

    execute_prompt(msg)


"""
Example with system, user and assistant messages
"""


def applying_user_assistant_examples():
    system_message_content = """You are a helpful geography tutor that generates concise summaries of 100 words for different
    countries. When asked about topics unrelated to geography respond with - 'I am not allowed to answer'"""
    msg: list[ChatCompletionMessageParam] = [
        system_message(system_message_content),
        user_message("What is the weather today?"),
        assistant_message("I am not allowed to answer"),
        user_message("Give me an overview of France"),
        assistant_message("France is a beautiful country. Paris is the capital of france"),
        user_message("Give me a summary of Spain's history"),
    ]
    execute_prompt(msg)


if __name__ == "__main__":
    ask_python_question()
    ask_question()
    applying_user_assistant_examples()
